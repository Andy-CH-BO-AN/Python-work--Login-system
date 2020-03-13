import requests
import datetime
from bs4 import BeautifulSoup


class Stock_requests():
    def __init__(self):
        self.res = requests.Session()
        self.header = {
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'}
        self.user_data = {}
        self.account_data = {}
        self.EntrustQuery_data = {}
        self.OrderRecord_data = {}
        self.InventoryDetail = {}
        self.ProfitLoss_accomplished = {}
        self.ProfitLoss_unaccomplished = {}
        self.ProfitLoss_unaccomplished_OrderId = {}
        self.GetProfitLossDetail_accomplished = {}
        self.GetProfitLossDetail_unaccomplished = {}
        self.GetStockPrice = {}
        self.user_id = None
        self.account_id = None
        self.account_pw = None
        self.Account_Name = None
        self.Account_ID = '小資族2'
        self.DelNum = None


    def login(self, UserId, PassWord):
        """登入"""
        url = 'https://www.cmoney.tw/member/login/?url=https%3a%2f%2fwww.cmoney.tw%2fvt%2faccount-manage.aspx'
        data = {
            '__VIEWSTATE': '/wEPDwULLTE3ODQzOTM2MTZkGAEFHl9fQ29udHJvbHNSZXF1aXJlUG9zdEJhY2tLZXlfXxYBBR9jdGwwMCRDb250ZW50UGxhY2VIb2xkZXIxJGNoZWNrnjqM86v4eHdkJ/obuwGou1QUFFg=',
            '__VIEWSTATEGENERATOR': '036ABEC6',
            '__EVENTVALIDATION': '/wEdAAWbXhdak0RUe49hHJhDm8G8u+smKTBNy/BiPEHoBzAYHE4Y+gq8lLFeXnTv49bJQt3IzSIt8diWVTTvtEzmzLT+oBzplOV7shwN8YmjJAmfvo89hdwioFYe1x1ZB79MF3Dl+IxC',
            'ctl00$ContentPlaceHolder1$account': '{}'.format(str(UserId)),
            'ctl00$ContentPlaceHolder1$pw': '{}'.format(str(PassWord)),
            'ctl00$ContentPlaceHolder1$loginBtn': '登入',
            'ctl00$ContentPlaceHolder1$check': 'on'
            }
        self.res.post(url, headers=self.header, data=data)
        url = 'https://www.cmoney.tw/vt/account-manage.aspx'
        res = self.res.get(url)
        html = BeautifulSoup(res.text)
        name = html.find_all('div', id='loginerNickName')
        for i in name:
            self.Account_Name = i.text
        if self.Account_Name != None and len(self.Account_Name) > 0 :
            return True
        return False


    def get_user_data(self):
        """取得用戶帳戶名字與ID"""
        print('-' * 50, '取得用戶帳戶名字與ID', '-' * 50)
        url = 'https://www.cmoney.tw/vt/account-manage.aspx'
        res = self.res.get(url)
        html = BeautifulSoup(res.text)
        data = html.find_all('div', class_='box-con')
        for i in data:
            self.user_data[i.find('a')['title']] = str(i.find('a')['href']).split('=')[1]

        money = html.find_all('div', class_='box-con')
        array = []
        for i in money:
            for ii in i.find_all('ul', class_='list1'):
                get = str(ii.text).split('\n')
                array.append(get[1:-1])

        for i in self.user_data:
            print(i, self.user_data[i])

        # print(self.user_data['小資族2'])
        return list(self.user_data), array


    def NewEntrust(self, code, price, ordqty, tradekind, bs_type):
        """下單"""

        if 500 > int(ordqty) > 0 and int(price) > 0:
            url = 'https://www.cmoney.tw/vt/ashx/userset.ashx?'
            data = {
                'act': 'NewEntrust',
                'aid': self.user_data[self.Account_ID],
                'stock': code,
                'price': price,
                'ordqty': ordqty,
                'tradekind': tradekind,
                'type': bs_type
                    }
            self.res.get(url, headers=self.header, data=data)
            return True
        return False

    def DeleteEntrust(self, order):
        """刪單"""
        user = self.user_data[self.Account_ID]
        for i in self.EntrustQuery_data[self.Account_ID]:
            print('第', i, '單', self.EntrustQuery_data[self.Account_ID][i])
        # order = int(input('刪除第幾單:'))
        url = 'https://www.cmoney.tw/vt/ashx/accountdata.ashx?act=DeleteEntrust&aid={}&GroupId=0&OrdNo={}'.format(user, self.EntrustQuery_data[self.Account_ID][order]['委託單號'])
        data = {
            'act': 'DeleteEntrust',
            'aid': 'user',
            'GroupId': '0',
            'OrdNo': self.EntrustQuery_data[self.Account_ID][order]['委託單號']
                }
        self.res.get(url, headers=self.header, data=data)
        return True
    def get_AccountInfo(self):
        """帳戶概覽"""
        print('-' * 50, '帳戶概覽', '-' * 50)
        # user = input('選擇使用者帳戶:')
        # print(self.user_data['小資族2'])
        # data = self.user_data['小資族2']
        # print(data)
        # user = '606661'
        user = self.user_data[self.Account_ID]
        url = 'https://www.cmoney.tw/vt/ashx/accountdata.ashx?act=AccountInfo&aid={}'.format(user)
        res = self.res.get(url).json()
        self.account_data['現金資產'] = res['Funds']
        # self.account_data['總資產'] = res['AllAssets']
        self.account_data['證券資產'] = res['InventoryValue']
        self.account_data['信用借款'] = res['Creditborrow']
        self.account_data['淨資產'] = res['AllAssets']
        self.account_data['獲利'] = res['Obtained']
        self.account_data['總報酬率'] = res['Ratio']
        self.account_data['整戶維持率'] = res['MaintenanceRate']

        chartInfo = str(res['ChartInfo']).replace('{"data":[', ''). \
            replace('"', ''). \
            replace(']}', ''). \
            replace('[', ''). \
            replace(']', ''). \
            split(',')
        # print(ChartInfo)
        accountdata = []
        for i in self.account_data:
            accountdata.append([i, self.account_data[i]])
        print(accountdata, chartInfo)
        return accountdata, chartInfo
    def get_EntrustQuery(self):
        """委託查詢"""
        print('-' * 50, '委託查詢', '-' * 50)
        for i in self.user_data:
            url = 'https://www.cmoney.tw/vt/ashx/accountdata.ashx?act=EntrustQuery&aid={}'.format(self.user_data[i])
            res = self.res.get(url).json()
            data = {}
            for ii, m in enumerate(res):
                data[ii+1] = {
                          '台股代號\n台股名稱': str(m['Id'])+ '\n' + m['Name'],
                          # '台股名稱': m['Name'],/
                          '交易類別': str(m['TkT']).split("'>")[1].split('</')[0].split('<')[0] + '\n' +
                                  str(m['TkT']).split("'>")[1].split('</')[0].split('>')[1],
                          '委託價': m['OrdPr'],
                          '委託量': m['OrdQty'],
                          '成交量': m['DeAvgPr'],
                          '成交均價': m['DeQty'],
                          '委託時間': str(m['Time']).split(' ')[0] + '\n' + str(m['Time']).split(' ')[1],
                          '委託狀態': str(m['StMsg']).replace('<span title="', '')[0:4],
                          '委託單號': m['CNo'],
                          }
            self.EntrustQuery_data[i] = data
        """下面for 看資料"""
        print(self.EntrustQuery_data)
        title = ['台股代號\n台股名稱', '交易類別', '委託價', '委託量', '成交量', '成交均價', '委託時間', '委託狀態', '刪單']
        return title, self.EntrustQuery_data[self.Account_ID]

    def get_OrderRecord(self):
        """交易紀錄"""
        print('-' * 50, '交易紀錄', '-' * 50)
        user = input('選擇使用者帳戶:')
        lookday = int(input('查詢天數:'))
        today = datetime.date.today()
        startTime = today - datetime.timedelta(days=lookday)
        url = 'https://www.cmoney.tw/vt/ashx/accountdata.ashx?act=OrderRecord&aid={}'.format(user)
        data = {'act': 'OrderRecord',
                'aid': user,
                'startTime': startTime,
                'endTime': today}
        res = self.res.get(url, data=data).json()
        for i, m in enumerate(res['data']):
            data = {
                    '台股代碼': m['Id'],
                    '台股名稱': m['Name'],
                    '交易類別': str(m['TkT']).split("'>")[1].split('</')[0].replace('<br>', ''),
                    '成交價': m['DealPr'],
                    '成交張數': m['DeQty'],
                    '手續費': int(''.join(str(m['Feecost']).split(','))),
                    '證交稅': int(''.join(str(m['Taxcost']).split(','))),
                    '借券費': int(''.join(str(m['SSFee']).split(','))),
                    '收付金額': int(''.join(str(m['ChangeAmount']).split(','))),
                    '時間': str(m['Time']).split('<')[1] + str(m['Time']).split('</')[0].split('>')[1]
                    }
            self.OrderRecord_data[i+1] = data
        print(self.OrderRecord_data)
        for i in self.OrderRecord_data:
            # print(i, self.OrderRecord_data[i])
            print(i,self.OrderRecord_data[i] )
        print(len(self.OrderRecord_data))
        all_Feecost = 0
        all_Taxcost = 0
        all_SSFee = 0
        all_ChangeAmount = 0
        for i in self.OrderRecord_data:
            all_Feecost += int(''.join(str(self.OrderRecord_data[i]['手續費']).split(',')))
            all_Taxcost += int(''.join(str(self.OrderRecord_data[i]['證交稅']).split(',')))
            all_SSFee += int(''.join(str(self.OrderRecord_data[i]['借券費']).split(',')))
            all_ChangeAmount += int(''.join(str(self.OrderRecord_data[i]['收付金額']).split(',')))
        total = ['合計', '', '', '', format(all_Feecost, ','), format(all_Taxcost, ','), format(all_SSFee, '',), format(all_ChangeAmount, ','), '']

        print(total)
        # print(data)
        # print(res['data'])

    def get_InventoryDetail(self):
        """庫存明細"""
        print('-' * 50, '庫存明細', '-' * 50)
        # url = 'https://www.cmoney.tw/vt/ashx/accountdata.ashx?act=InventoryDetail&aid=605587'
        user = input('選擇使用者帳戶:')
        url = 'https://www.cmoney.tw/vt/ashx/accountdata.ashx?act=InventoryDetail&aid={}'.format(user)
        res = self.res.get(url).json()
        for i, m in enumerate(res):
            data = {
                '台股代碼': m['Id'],
                '台股名稱': m['Name'],
                '倉別': m['TkT'],
                '庫存': m['IQty'],
                '可交易': m['TodayQty'],
                '平均成本': m['DeAvgPr'],
                '現價': m['NowPr'],
                '預估損益': m['IncomeLoss'],
                '報酬率': m['Ratio']
                    }
            self.InventoryDetail[i+1] = data
        for i in self.InventoryDetail:
            print(i)
            for ii in self.InventoryDetail[i]:
                print(ii, self.InventoryDetail[i][ii])

    def get_ProfitLoss_accomplished(self):
        """損益試算  未實現損益"""
        print('-' * 50, '損益試算  未實現損益', '-' * 50)
        url = 'https://www.cmoney.tw/vt/ashx/accountdata.ashx?act=ProfitLoss&aid=606661&profitLossType=unaccomplished'
        # user = input('選擇使用者帳戶:')
        # url = 'https://www.cmoney.tw/vt/ashx/accountdata.ashx?act=ProfitLoss&aid={}&profitLossType=unaccomplished'.format(user)
        res = self.res.get(url).json()

        for i, m in enumerate(res):
            data = {
                '台股代碼': m['Id'],
                '台股名稱': m['Name'],
                '倉別': m['TkT'],
                '張數': m['IQty'],
                '可平倉': m['TodayQty'],
                '買賣均價': m['DeAvgPr'],
                '現價': m['NowPr'],
                '買入成本': m['Cost'],
                '預估賣出收入': m['PredictionIncome'],
                '損益': m['IncomeLoss'],
                '報酬率': m['Ratio']
                }
            self.ProfitLoss_accomplished[i+1] = data
        for i in self.ProfitLoss_accomplished:
            print(i, self.ProfitLoss_accomplished[i])
        all_Cost = 0
        all_PredictionIncome = 0
        all_IncomeLoss = 0
        for i in self.ProfitLoss_accomplished:
            all_Cost += int(''.join(str(self.ProfitLoss_accomplished[i]['買入成本']).split(',')))
            all_PredictionIncome += int(''.join(str(self.ProfitLoss_accomplished[i]['預估賣出收入']).split(',')))
            all_IncomeLoss += int(''.join(str(self.ProfitLoss_accomplished[i]['損益']).split(',')))
        all_Ratio = all_IncomeLoss / all_Cost * 100
        print(['合計', '', '', format(all_Cost, ','), format(all_PredictionIncome, ','), format(all_IncomeLoss, ','), '%.2f' % all_Ratio, '', ''])

    def get_GetProfitLossDetail_unaccomplished(self):

        url = 'https://www.cmoney.tw/vt/ashx/accountdata.ashx?act=GetProfitLossDetail&profitLossType=unaccomplished'
        Id = '2618'
        data = {
                'act': 'GetProfitLossDetail',
                'profitLossType': 'unaccomplished',
                'aid': '605587',
                'commkey': Id
                }
        res = self.res.get(url, data=data).json()
        print(res)
        for i in res:

            data = {
                '台股代碼': i['Id'],
                '台股名稱': i['Name'],
                '倉別': i['TkT'],
                '張數': i['IQty'] + '張',
                '預估手續費': i['Feecost'],
                '預估交易稅': i['Taxcost'],
                '預估借券費': i['ShortSellingFee'],
                '預估損益': i['IncomeLoss'],
                '預估報酬率': str(i['Ratio']).split("'>")[1].split('<')[0],
                '時間': str(i['Time']).split('<')[0] + '\n' + str(i['Time']).split('>')[1]
                    }
        self.GetProfitLossDetail_unaccomplished[Id] = data

        for i in self.GetProfitLossDetail_unaccomplished:

            for ii in self.GetProfitLossDetail_unaccomplished[i]:
                print(ii, self.GetProfitLossDetail_unaccomplished[i][ii])

    def get_ProfitLoss_unaccomplished(self):
        """損益試算  已實現損益"""
        print('-' * 50, '損益試算  已實現損益', '-' * 50)
        url = 'https://www.cmoney.tw/vt/ashx/accountdata.ashx?act=ProfitLoss&aid=605587&profitLossType=accomplished'
        # user = input('選擇使用者帳戶:')
        # lookday = int(input('查詢天數:'))
        # today = datetime.date.today()
        # startTime = today - datetime.timedelta(days=lookday)
        # url = 'https://www.cmoney.tw/vt/ashx/accountdata.ashx?act=ProfitLoss&aid={}&profitLossType=accomplished'.format(user)
        data = {'act': 'ProfitLoss',
                'aid': '605587',
                'profitLossType': 'accomplished',
                'startTime': '2019-11-1',
                'endTime': '2020-1-30'}
        res = self.res.get(url, data=data).json()

        # print(res)
        for i, m in enumerate(res):
            data = {
                '台股代碼': m['Id'],
                '台股名稱': m['Name'],
                '倉別': m['TkT'],
                '張數': m['IQty'] + '張',
                '買入成本': m['BuyTotal'],
                '賣出收入': m['SellTotal'],
                '損益': m['IncomeLoss'],
                '報酬率': m['Ratio']
                    }
            self.ProfitLoss_unaccomplished[i+1] = data
            data = {'單號': m['OrderId']}
            self.ProfitLoss_unaccomplished_OrderId[i+1] = data

        for i in range(len(self.ProfitLoss_unaccomplished)):
            print(self.ProfitLoss_unaccomplished[i+1])
            print(self.ProfitLoss_unaccomplished_OrderId[i+1])
        all_BuyTotal = 0
        all_SellTotal = 0
        all_IncomeLoss = 0
        for i in self.ProfitLoss_unaccomplished:
            all_BuyTotal += int(''.join(str(self.ProfitLoss_unaccomplished[i]['買入成本']).split(',')))
            all_SellTotal += int(''.join(str(self.ProfitLoss_unaccomplished[i]['賣出收入']).split(',')))
            all_IncomeLoss += int(''.join(str(self.ProfitLoss_unaccomplished[i]['損益']).split(',')))
        # print(all_IncomeLoss)

        all_Ratio = all_IncomeLoss / all_BuyTotal * 100
        print(['合計', '', '', format(all_BuyTotal, ','), format(all_SellTotal, ','), format(all_IncomeLoss, ','), '%.2f' % all_Ratio, '', ''])

    def get_GetProfitLossDetail_accomplished(self):
        """損益試算  已實現損益  取得明細"""
        print('-' * 50, '損益試算  已實現損益', '-' * 50)
        url = 'https://www.cmoney.tw/vt/ashx/accountdata.ashx?act=GetProfitLossDetail&profitLossType=accomplished&orderNo=20764232'
        # url = 'https://www.cmoney.tw/vt/ashx/accountdata.ashx?act=GetProfitLossDetail&profitLossType=accomplished&orderNo={}'.format(self.ProfitLoss_unaccomplished_OrderId[''])

        res = self.res.get(url).json()
        # print(res)
        for i, m in enumerate(res):
            data = {
                '台股代碼': m['Id'],
                '倉別': m['TkT'],
                '賣價': m['SellPr'],
                '買價': m['BuyPr'],
                '帳面收入': m['SellTotal'],
                '投資成本': m['BuyTotal'],
                '損益': m['IncomeLoss'],
                '報酬率': str(m['Ratio']).split("'>")[1].split('<')[0],
                '時間': str(m['Time']).split('<')[0] + '\n' + str(m['Time']).split('>')[1]
                }
            self.GetProfitLossDetail_accomplished[i+1] = data

    def get_GetStockPrice(self, code):
        """看五買五賣"""
        # code = '2330'

        url = 'https://www.cmoney.tw/vt/ashx/HandlerGetStockPrice.ashx?q={}&accountType=7'.format(code)
        res = requests.get(url).json()
        # print(res)
        # data = {}
        data = []
        for i in range(1, 6):
            # data['買{}量'.format(str(i))] = str(int(res['StockInfo']['BuyQty{}'.format(str(i))]))
            # data['買{}'.format(str(i))] = res['StockInfo']['BuyPr{}'.format(str(i))]
            # data['賣{}'.format(str(i))] = res['StockInfo']['SellPr{}'.format(str(i))]
            # data['賣{}量'.format(str(i))] = str(int(res['StockInfo']['SellQty{}'.format(str(i))]))
            get = ['買{}量'.format(str(i))] + [str(int(res['StockInfo']['BuyQty{}'.format(str(i))]))] + \
                  ['買{}'.format(str(i))] + [str(res['StockInfo']['BuyPr{}'.format(str(i))])] + \
                  ['賣{}'.format(str(i))] + [str(res['StockInfo']['SellPr{}'.format(str(i))])] + \
                  ['賣{}量'.format(str(i))] + [str(int(res['StockInfo']['SellQty{}'.format(str(i))]))]
            data.append(get)
        # for i in data:
        #     print(i, data[i])
        print(data)
        # print(list(data))
        return data

if __name__ == '__main__':
    stock = Stock_requests()
    i = '0912001585'
    p = '1qaz2wsx3edc'
    stock.login(i, p)
    stock.get_user_data()
    stock.get_EntrustQuery()
    stock.DeleteEntrust()
    # print(stock.get_user_data())
    # stock.get_AccountInfo()
    # print(stock.get_AccountInfo())
    # print(type(t))
    # print(t[1])
    # print(t[1])
    # t = stock.get_EntrustQuery()
    # print(t[1])
    # for i in range(len(t[1])):
    #     num = 0
    #     # print(t[1][i+1])
    #     for ii in t[1][i+1]:
    #         print(t[1][i+1][ii])



    # stock.get_OrderRecord()
    # stock.get_InventoryDetail()
    # stock.get_ProfitLoss_accomplished()
    # stock.get_ProfitLoss_unaccomplished()
    # stock.get_GetProfitLossDetail_accomplished()
    # stock.get_GetProfitLossDetail_unaccomplished()
    # stock.get_GetStockPrice()
    # for i in range(6):
    #     stock.NewEntrust()
    # day = date.today()
    # a = day - timedelta(days=7)
    # print(a)
    # a = (['小資族2', '小資族23', '小資族'], [['總資產：$1,858,015', '投資報酬率：-7.10%', '追蹤人數：0人'], ['總資產：$1,831,506', '投資報酬率：-8.42%', '追蹤人數：0人'], ['總資產：$1,860,531', '投資報酬率：-6.97%', '追蹤人數：0人']])
    # print(a[1][0][0])

    # act: NewEntrust
    # aid: 606661
    # stock: 2231
    # price: 216.5
    # ordqty: 1
    # tradekind: c
    # type: s
    # hasWarrant: true
    # act: NewEntrust
    # aid: 606661
    # stock: 2231
    # price: 216.5
    # ordqty: 1
    # tradekind: c
    # type: b
    # hasWarrant: true
    #
    # act: NewEntrust
    # aid: 606661
    # stock: 2231
    # price: 216.5
    # ordqty: 1
    # tradekind: cd
    # type: b
    # hasWarrant: true
    # act: NewEntrust
    # aid: 606661
    # stock: 2231
    # price: 216.5
    # ordqty: 1
    # tradekind: cd
    # type: s
    # hasWarrant: true
    #
    # act: NewEntrust
    # aid: 606661
    # stock: 2231
    # price: 216.5
    # ordqty: 1
    # tradekind: sd
    # type: s
    # hasWarrant: true
    # act: NewEntrust
    # aid: 606661
    # stock: 2231
    # price: 216.5
    # ordqty: 1
    # tradekind: sd
    # type: b
    # hasWarrant: true