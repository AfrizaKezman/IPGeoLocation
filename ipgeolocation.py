__author__  = 'cybot101'


import sys, os
from core.IpGeoLocationLib import IpGeoLocationLib
from core.Logger import Logger
from core.Menu import parser,args,banner
    
def main():

    # no args provided
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)
    
    logsDir = os.path.join(os.getcwd(), 'logs')
    #resultsDir = os.path.join(os.getcwd(), 'results')
    if not os.path.exists(logsDir):
        os.mkdir(logsDir)
    #if not os.path.exists(resultsDir):
    #    os.mkdir(resultsDir)
        
    logger = Logger(args.nolog, args.verbose)
    
    #single target or multiple targets 
    if(args.target and args.tlist):
        logger.PrintError("You can request Geolocation information either for a single target(-t) or a list of targets(-T). Not both!", args.nolog)
        sys.exit(2)
        
    #my ip address or single target
    if(args.target and args.myip):
        logger.PrintError("You can request Geolocation information either for a single target(-t) or your own IP address. Not both!", args.nolog)
        sys.exit(3)
        
    #multiple targets or my ip address
    if(args.tlist and args.myip):
        logger.PrintError("You can request Geolocation information either for a list of targets(-T) or your own IP address. Not both!", args.nolog)
        sys.exit(4)
    
    #single target and google maps only allowed
    if(args.tlist and args.g):
        logger.PrintError("Google maps location is working only with single targets.", args.nolog)
        sys.exit(5)
    
    #specify user-agent or random
    if(args.uagent and args.ulist):
        logger.PrintError("You can either specify a user-agent string or let IPGeolocation pick random user-agent strings for you from a file.", args.nolog)
        sys.exit(6)
        
    #specify proxy or random
    if(args.proxy and args.xlist):
        logger.PrintError("You can either specify a proxy or let IPGeolocation pick random proxy connections for you from a file.", args.nolog)
        sys.exit(7)
        
        
    #init lib
    ipGeoLocRequest = IpGeoLocationLib(args.target, logger, args.noprint)
    
    print(banner)
    
    #retrieve information
    if not ipGeoLocRequest.GetInfo(args.uagent, args.tlist, 
                                     args.ulist, args.proxy, args.xlist,
                                     args.csv, args.xml, args.txt, args.g):
        logger.PrintError("Retrieving IP Geolocation information failed.")
        sys.exit(8)


if __name__ == '__main__':
    main()
    