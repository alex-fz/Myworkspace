import cProfile
import main
import unittest
import time
from memory_profiler import profile

class MyTest(unittest.TestCase):
    testing = main.WorkCsv()
    #Uncomment the below line for memory profile
    #@profile 
    def test_english_dictionary(self):
        
        before_months = {'January':'','February':'','March':'','April':'','May':'','June':'',
                        'July':'','August':'','Septembre':'','October':'','November':'','December':''}

        self.testing.obtain_months_name()
        print(self.testing.english_months)
        print(before_months)

        self.assertNotEqual(before_months, self.testing.english_months)
    #Uncomment the below line for memory profile
    #@profile
    def test_time(self):
        starter_time = time.time()
        main.main()
        final_time = time.time() - starter_time
        self.assertLess(final_time, 1.5)
        print('It took %s seconds to finish the test'%final_time)


    def test_results(self):
        pass

    




if __name__ == '__main__':
    profiler = main.WorkCsv()
    
    cProfile.run('main.main()')