import csv
import speedtest
import time
# import twitter
 
def test():
    while True:
        s = speedtest.Speedtest()
        s.get_best_server()
        s.download()
        s.upload()
        s.results.share()

        results_dict = s.results.dict()
        print(results_dict)

        results_dict["download"]
        with open("data.csv","a",newline='') as out_file:
            out_file = csv.writer(out_file)
            out_file.writerow((time.strftime("%a, %d %b %Y %H:%M:%S"),results_dict["download"],results_dict["upload"],results_dict["ping"]))

        time.sleep(10)

       
if __name__ == '__main__':
        test()