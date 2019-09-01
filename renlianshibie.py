# -*- coding: utf-8 -*-
"""
Created on Wed Jan  9 10:57:27 2019

@author: caiyu
"""
import requests
def detect_face(image_url,
                api_key="KzPAQJoozgoXNvnTFrDHPy2d1RbbKiLd",
                api_secret="BeuZIC6hkLV4wKc_YniW33yIwJnp8UlJ",
                return_landmark=1,
                return_attributes="gender,age,smiling"):
        url="http://img.mingxing.com/upload/attach/2015/06-26/291231-WjbCM8.jpg"
        params={"api_key":api_key,
                "api_secret":api_secret,
                "image_url":image_url,
                "return_landmark":return_landmark,
                "return_attributes":return_attributes
                }
        
        r=requests.post(url=url,params=params)
        return r

        






