# -*- coding: utf-8 -*-
import twython
import ConfigParser

if __name__ == '__main__':
    tweet_str = "テスト"

    config_file = ConfigParser.SafeConfigParser()
    config_file.read(".twitter_config")

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
