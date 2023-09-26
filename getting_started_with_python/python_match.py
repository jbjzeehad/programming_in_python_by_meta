http_status = 500

if http_status == 200 or http_status == 201:
    print('Sucess')
elif http_status == 400:
    print('Bad Request')
elif http_status == 404:
    print('Not Found')
elif http_status == 500 or http_status == 501:
    print('Server Error')
else:
    print('Unknown')


match http_status:  # switch
    case 200 | 201:
        print('Success')
    case 500 | 501:
        print('Server Error')
    case 400:
        print('Bad Request')
    case _:
        print('Unknown')
