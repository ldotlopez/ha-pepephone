VALID_LOGIN_RESPONSE = (
    b"{"
    b'"accessToken": "eyJ0eXAi", '
    b'"tokenType": "Bearer", '
    b'"expiresIn": 4200, '
    b'"jwt": "Xdka2hGc"'
    b"}"
)

INVALID_LOGIN_RESPONSE = (
    b'{"uuid":"bfa49673-4404-44fe-957b-c189d1218c2b","error":{"code":20004,"messag'
    b'e":"Bad credentials","description":null}}'
)

PRODUCTS_INFO = (
    b'{"mobile":[{"productType":"MOVIL","msisdn":"600111222","code":"1234","alias"'
    b':"","slug":null,"channel":"BOC","icc":"***************1234","puk":"****1234"'
    b',"lineType":"VOZ_DATOS_6.9_4GB","flatRate":true,"portabilityStatus":"APOR","'
    b'portabilityDate":"01\\/02\\/1995","rate":"Tarifa 0 cent min","promotionCod'
    b'e":"ABCD4QWERTY3","promotion":"Habla por 0 cents\\/min y Navega 4GB","pro'
    b'motionDetail":{"maxDataVolume":4096,"maxDuration":0,"price":5.7025,"priceWit'
    b'hTax":6.9,"priceVoice":0,"priceVoiceWithTax":0,"minutePrice":0.006,"minutePr'
    b'iceWithTax":0.0073},"flatRateDescription":"TP 4GB (6.9E)","sharedFlatRate":{'
    b'"master":"","slave":""},"dataMax":"4096","onlyData":false,"invoices":[{"numb'
    b'er":"123456789012345","date":"28\\/02\\/2022","type":"ME","total":12.34,"l'
    b'ines":["600111222"],"addresses":[]},{"number":"123456789012345","date":"'
    b'31\\/01\\/2022","type":"ME","total":11.49,"lines":["600111222"],"addresses'
    b'":[]}],"viewType":1,"signupChannel":"","salePointCode":"","tariffChange":{"s'
    b'tatus":null,"promotionCode":null,"date":null},"paymentType":"D","convergence'
    b'Id":"","signUpDate":1531227556,"discounts":[],"simReplacement":{"simType":""'
    b',"icc":"","status":"","date":null},"id":"600111222","status":"A","subStatus"'
    b':"A"}],"broadband":[],"fixed":[],"energy":[],"errors":[],"dashboardItems":[{'
    b'"category":"MO","groupName":"M\\u00f3vil","groupItems":[{"productType":"M'
    b'OVIL","id":"600111222","description":"M\\u00f3vil","info":"600111222"}]}]'
    b',"invoices":[{"serviceType":"PPH","type":"ME","date":1646053169,"total":12.3'
    b"4}]}"
)

PRODUCT_DETAILS = (
    b'{"data":{"total":{"total":0,"consumed":1588.89,"cost":0},"national":{"total"'
    b':4293,"consumed":1588.89,"cost":6.9},"flatNational":{"total":4096,"consumed"'
    b':1391.89,"cost":6.9},"flatRlah":{"total":4096,"consumed":0,"cost":0},"subord'
    b'inate":{"total":0,"consumed":0,"cost":0},"rlah":{"total":4293,"consumed":0,"'
    b'cost":0},"roaming":{"total":0,"consumed":0,"cost":0},"withCost":{"total":0,"'
    b'consumed":0,"cost":0},"noCost":{"total":197,"consumed":197,"cost":0},"dailyA'
    b'ctive":false,"daily":{"total":0,"consumed":0,"cost":0},"dailyRlah":{"total":'
    b'0,"consumed":0,"cost":0},"bundles":[{"code":2739974,"type":"GM","typeId":8,"'
    b'usagePeriod":"M","description":"AcumulaMegas","purchaseCount":1,"priority":-'
    b'1,"finished":true,"price":0,"dataTotal":197,"dataRlah":197,"consumptionRlah"'
    b':0,"consumptionNational":197,"consumptionNationalSub":0,"consumptionRlahSub"'
    b':0,"free":true}],"lowSpeed":0,"infinite":{"active":false,"purchased":false}}'
    b',"voice":{"flatNational":{"seconds":0,"price":0},"national":{"seconds":0,"pr'
    b'ice":1.6335},"international":{"seconds":0,"price":0},"special":{"seconds":0,'
    b'"price":0},"rlah":{"seconds":0,"price":0},"roaming":{"seconds":0,"price":0},'
    b'"flatRate":false,"total":1.6335},"sms":{"count":0,"price":0},"dataFlat":4096'
    b',"dataFlatRlah":4096,"voiceFlatPrice":0,"dataExtraMbPrice":0.04,"dataConsume'
    b'All":1588.89,"dataConsume":1588.89,"dataConsumeRoaming":0,"dataConsumeRoamin'
    b'gRlah":0,"dataConsumePercent":37.01,"dataConsumeSub":0,"dataConsumeRoamingSu'
    b'b":0,"dataConsumeRoamingRlahSub":0,"dataConsumePercentSub":0,"dataAmount":6.'
    b'9,"voiceFlat":0,"dataFlatPrice":6.9,"voiceConsume":529,"voiceConsumeFlatIncl'
    b'uded":0,"voiceConsumeFlatExcess":0,"voiceConsumeNational":529,"voiceConsumeI'
    b'nternational":0,"voiceConsumeSpecial":0,"voiceConsumeRoaming":0,"voiceConsum'
    b'eRoamingRlah":0,"voiceAmount":1.6335,"voiceAmountInternational":0,"voiceAmou'
    b'ntNational":1.6335,"voiceAmountSpecial":0,"voiceAmountRoaming":0,"voiceAmoun'
    b'tRoamingRlah":0,"smsCount":0,"smsAmount":0,"bundles":[{"code":"2739974","typ'
    b'e":"GM","bundleType":8,"count":1,"purchaseCount":1,"endDate":1646179199,"dat'
    b'a":197,"dataRlah":197,"price":0,"dataConsume":197,"dataConsumeRlah":0,"activ'
    b'e":true,"finished":true,"applicationPeriod":"M","description":"AcumulaMegas"'
    b',"priority":-1}]}'
)

INVALID_PRODUCT_RESPONSE = (
    b'{"uuid":"2be7c6e7-16be-4ea4-81e4-1f4db5e44b42","error":{"code":10404,"messag'
    b'e":"No route found for \\"GET \\/api\\/consumption\\/123456789\\"","desc'
    b'ription":null}}'
)
