import requests




def get_smelting_cost():
    try:
        url = 'https://api.mir4global.com/wallet/prices/derby'
        resp = requests.post(url)
        jsonresp = resp.json()
        dados = jsonresp["Data"]
        lastdados = dados[-1]
        ds = (lastdados["DS"])
        smlt = (lastdados["SmeltingCost"])
        value = int(smlt) + int(ds)
        return value
    except:
        print('Sem código')
        return None
