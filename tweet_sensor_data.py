# -*- coding: utf-8 -*-
import twython
import ConfigParser
import get_sensor_data as gsd
from os import path

if __name__ == '__main__':
    gsd.readData()

    # time_str = datetime.datetime.today().strftime("%Y/%m/%d %H:%M:%S")
    temp_str = str("{0:.1f}".format(gsd.sensor_data['temp']))
    humid_str = str("{0:.1f}".format(gsd.sensor_data['humidity']))
    pressure_str = str("{0:.1f}".format(gsd.sensor_data['pressure']))

    tweet_str = "現在の温度は"+temp_str+"度 湿度は"+humid_str+"％ 気圧は"+pressure_str+"hPa です"+'\r\n'
    if gsd.sensor_data['temp'] > 25:
        tweet_str += "暑いですね"+'\r\n'

    if gsd.sensor_data['temp'] < 10:
        tweet_str += "寒いですね"+'\r\n'
 
    if gsd.sensor_data['humidity'] > 60:
        tweet_str += "むしむししますね"+'\r\n'

    # print(tweet_str)
    
    config_file = ConfigParser.SafeConfigParser()
    config_file_path = path.dirname(path.abspath( __file__ )) + "/.twitter_config"
    config_file.read(config_file_path)
    
    consumerKey = config_file.get("settings","consumerKey")
    consumerSecret = config_file.get("settings","consumerSecret")
    accessToken = config_file.get("settings","accessToken")
    accessSecret = config_file.get("settings","accessSecret")
    
    api = twython.Twython(app_key=consumerKey,
                  app_secret=consumerSecret,
                  oauth_token=accessToken,
                  oauth_token_secret=accessSecret)
    
    try:
        api.update_status(status=tweet_str)
    except twython.TwythonError as e:
        print e
