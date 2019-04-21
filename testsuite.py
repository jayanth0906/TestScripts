from unittest import TestLoader, TestSuite, TextTestRunner
from addcust import Add_Customer
from editcust import Editcustomer
from deletecust import DeleteCutomer
from portfolio import Portfolio
from addinvest import AddInvestment
from editinvest import Editinvestment
from deleteinvest import Deleteinvestment
from addstock import Addstock
from editstock import Editstock
from deletestock import Deletestock

if __name__ == "__main__":
    loader = TestLoader()
    suite = TestSuite((
        loader.loadTestsFromTestCase(Add_Customer),
        loader.loadTestsFromTestCase(Editcustomer),
        loader.loadTestsFromTestCase(DeleteCutomer),
        loader.loadTestsFromTestCase(Portfolio),
        loader.loadTestsFromTestCase(AddInvestment),
        loader.loadTestsFromTestCase(Editinvestment),
        loader.loadTestsFromTestCase(Deleteinvestment),
        loader.loadTestsFromTestCase(Addstock),
        loader.loadTestsFromTestCase(Editstock),
        loader.loadTestsFromTestCase(Deletestock),


    ))

    runner = TextTestRunner(verbosity=2)
    runner.run(suite)
