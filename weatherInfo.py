from bs4 import BeautifulSoup
import datetime
import requests
import os
#Bangalore

class WeatherForecast:
    def __init__(self,url):
        self.url = url
    
    def GetWeatherInfo(self):
        r = requests.get(self.url)
        soup = BeautifulSoup(r.content,'html.parser')
        print '\n\t\t' + soup.title.string + '\n\t\t'
        data = soup.find("div",class_="info")
        get_weather = data.get_text()
        print '-'*20
        return get_weather.encode('utf-8')
def sstring():
    print '-' * 20

      


def kar_region():
    
    
    print 'Welcome to weather forecasting'
    print '1. Bangalore'
    print '2. Belgaum'
    print '3. Mangalore'
    print '4. Hubli'
    print '5. Gulbarg'
    print '6. Hassan District'
    print '7. Bijapur'
    print '8. Tumkur'
    print '9. Hospet'
    print '10. Myosre'
    print '11. Dharwad'
    print '12. Udupi'
    print '13. Gadag Betagiri'
    print '14. Mandya District'
    print '15. Belur'
    print '16. Srirangapatna'
    print '17. Hampi'
    print '18 Madikeri'
    print '19. Badami'
    print '20. GangaVati Karnataka'
    print '21. Bhadravati Karnataka'
    print '22. Bijapur District'
    print '23. Karwar'
    print '24. Gulbarga District'
    print '25. Pattadakal'
    print '26. Gulbarg District'
    print '27. Pattadakal'
    print '28. Sirsi'
    print '29. Halebidu'
    print '30. Yadgir'
    print '31. Uttara Kannada'
    print '32. Sandur'
    print '33. Bangarpet'
    print '34. Channapatna'
    print '35. Basvakalyan'
    print '36. Gokak'
    print '37. Aihole'
    print '38. Sringeri'
    print '39. Karkala'
    print '40. Nargund'
    print '41. kanakpura'
    print '42. Hangal'
    print '43. Raichur'
    print '44. Gunduplet'
    print '45. Kolar District'
    print '46. Chitradurga District'
    print '47. Gadag District'
    print '48. Bangalore Rural District'

   
    return "End Of List"

#Karnataka state
print '1. Karnataka'

state = int(raw_input("Enter State name "))
if state == 1:
    print kar_region()
    usr_input = int(raw_input("Please select city "))
    if usr_input == 1:
        #Instance Bangalore
        bangalore = WeatherForecast("http://www.accuweather.com/en/in/bengaluru/204108/weather-forecast/204108")
        print bangalore.GetWeatherInfo()
        print '-' * 20
    elif usr_input == 2:
        #Instance Belgaum
        belagum =  WeatherForecast("http://www.accuweather.com/en/in/belgaum/188752/weather-forecast/188752")
        print belagum.GetWeatherInfo()  
        print '-' * 20
    elif usr_input == 3:
        #instance Mangalore
         mangalore = WeatherForecast("http://www.accuweather.com/en/in/mangalore/188760/weather-forecast/188760")
         print mangalore.GetWeatherInfo()
         print '-' * 20
    elif usr_input == 4:
         hubli = WeatherForecast("http://www.accuweather.com/en/in/hubli-dharwad/3352291/weather-forecast/3352291")
         print hubli.GetWeatherInfo()
         print '-' * 20
    elif user_inpu == 5:
         gulbarg = WeatherForecast("http://www.accuweather.com/en/in/gulbarga/188754/weather-forecast/188754")
         print gulbarg.GetWeatherInfo() 
         print '-' * 20
    elif usr_input == 6:
         assan_district = WeatherForecast("http://www.accuweather.com/en/in/hassan/2864133/weather-forecast/2864133")
         print assan_district.GetWeatherInfo()
         print '-' * 20
    elif usr_input == 7:
         bijapur =  WeatherForecast("http://www.accuweather.com/en/in/bijapur/188755/weather-forecast/188755")
         print bijapur.GetWeatherInfo()
         print '-' * 20
    elif usr_input == 8:
         tumkur  = WeatherForecast("http://www.accuweather.com/en/in/tumkur/188762/weather-forecast/188762")
         print tumkur.GetWeatherInfo()
         print '-' * 20 
    elif usr_input == 9:
         hospet = WeatherForecast("http://www.accuweather.com/en/in/hospet/188758/weather-forecast/188758")
         print hospet.GetWeatherInfo()
         print   '-' * 20
    elif usr_input == 10:
         mysore = WeatherForecast("http://www.accuweather.com/en/in/mysore/204111/weather-forecast/204111")
         print mysore.GetWeatherInfo()
         print '-' * 20
    elif usr_input == 11:
        dharwad = WeatherForecast("")
        print dharwad.GetWeatherInfo()
    elif usr_input == 12:
        udupi = WeatherForecast("")
        print udupi.GetWeatherForecast()
        print '-' * 20
    elif usr_input == 13:
        gadag = WeatherForecast("")
        print gadag.GetWeatherForecast("")
    elif usr_input == 14:
        mandya = WeatherForecast("")
        print mandya.GetWeatherForecast()
    elif usr_input == 15:
        belur = WeatherForecast("")
    elif usr_input == 16:
        srirangapatna = WeatherForecast("")
        srirangapatna.GetWeatherForecast()
        print '-' * 20
    elif usr_input == 17:
        hampi = WeatherForecast("")
        print hampi.GetWeatherForecast()
        print '-' * 20
    elif usr_input == 18:
        madikeri = WeatherForecast("")
        print madikeri.GetWeatherForecast()
    elif usr_input == 19:
        badami = WeatherForecast("")
        print badami.GetWeatherForecast()
    elif  usr_input == 20:
        gangavati = WeatherForecast("")
        print gangavati.GetWeatherForecast()
        print '-' * 20
    elif usr_input == 21:
        bhardavati = WeatherForecast("")
        print bhardavati.GetWeatherForecast("")
        print '-' * 20
    elif usr_input == 22:
        bijapur = WeatherForecast("")
        print bijapur.GetWeatherForecast()
        print '-' * 20
    elif usr_input == 23:
        karwar = WeatherForecast("")
        print karwar.GetWeatherForecast()
        print '-' * 20
    elif usr_input == 24:
        gulbarg = WeatherForecast("")
        print gulbarg.GetWeatherForecast()
        print '-' * 20
    elif usr_input == 25:
        pattadakal = WeatherForecast("")
        print pattadakal.GetWeatherForecast()
        print '-' * 20
    elif usr_input == 26:
        sirsi = WeatherForecast("")
        print sirsi.GetWeatherInfo()
        print '-' * 20
    elif usr_input == 27:
        pattadakal = WeatherForecast("")
        print pattadakal.GetWeatherInfo()
        print '-' * 20
    elif usr_input == 28:
        sirsi = WeatherForecast("")
        print sirsi.GetWeatherInfo()
        print '-' * 20
    elif  usr_input == 29:
        halebidu = WeatherForecast("")
        print halebidu.GetWeatherInfo()
        print '-' * 20
    elif usr_input == 30:
        yadgir = WeatherForecast("")
        print yadgir.GetWeatherInfo()
        print sstring()
    elif usr_input == 31:
        uttara = WeatherForecast("")
        print uttara.GetWeatheForecast()
        print sstring()
    elif usr_input == 32:
        sandur = WeatherForecast("")
        print sandur.GetWeatheForecast()
        print sstring()
    elif usr_input == 33:
        bangarpet = WeatherForecast("")
        print bangarpet.GetWeatheForecast()
        print sstring()
    elif usr_input == 34:
        channapatna  = WeatherForecast("")
        print channapatna.GetWeatheForecast()
        print sstring()
    elif usr_input == 35:
        basvakalyan = WeatherForecast("")
        print basvakalyan.GetWeatheForecast()
        print sstring()
    elif usr_input == 36:
        Gokak = WeatherForecast("")
        print Gokak.GetWeatheForecast()
        print sstring()
    elif usr_input == 37:
        Aihole = WeatherForecast("")
        print Aihole.GetWeatheForecast()
        print sstring()
    elif usr_input == 38:
        Sringeri = WeatherForecast("")
        print Sringeri.GetWeatheForecast()
        print sstring()
    elif usr_input == 39:
        Karkala = WeatherForecast("")
        print Karkala.GetWeatheForecast()
        print sstring()
    elif usr_input == 40:
        Nargund = WeatherForecast("")
        print Nargund.GetWeatheForecast()
        print sstring()
    elif usr_input == 41:
        kanakpura = WeatherForecast("")
        print kanakpura.GetWeatheForecast()
        print sstring()
    elif usr_input == 42:
        Hangal = WeatherForecast("")
        print Hangal.GetWeatheForecast()
        print sstring()
    elif usr_input == 43:
        Raichur = WeatherForecast("")
        print Raichur.GetWeatheForecast()
        print sstring()
    elif usr_input == 44:
        Gunduplet = WeatherForecast("")
        print Gunduplet.GetWeatheForecast()
        print sstring()
    elif usr_input == 45:
        Kolar = WeatherForecast("")
        print Kolar.GetWeatheForecast()
        print sstring()

    elif usr_input == 46:
        Chitradurga = WeatherForecast("")
        print Chitradurga.GetWeatheForecast()
        print sstring()

    elif usr_input == 47:
        Gadag = WeatherForecast("")
        print Gadag.GetWeatheForecast()
        print sstring()
    elif usr_input == 48:
        Bangalore_rural = WeatherForecast("")
        print Bangalore_rural.GetWeatheForecast()
        print sstring()
''' END 
		OF
			BANGALORE
			           REGION
'''


        
        



        
     
