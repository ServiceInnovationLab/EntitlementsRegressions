import unittest
import requests

class TestAccomodationSupplement(unittest.TestCase):

  def testBasic(self):
    url = 'https://nz.raap.d61.io/api/v0/domain/nz-entitlements-eligibility/reasoning/reason?criteria=draft'
    token = 'TOKEN'
    headers = {'Content-Type': 'application/json','Authorization': 'Bearer {token}'.format(token=token)}

    print headers
    result = requests.post(url, headers=headers);
    print(result.status_code)
    print(result.text)

    self.assertTrue(False)

if __name__ == '__main__':
    unittest.main()