from numpy import sqrt, exp, pi, log10, sin

def CC_nongui(z=None, H0 = None, WM = None, WV = None):
    try:
        float(H0)
    except:
        print "Valid H0 value not provided Default H0 = 71.0"
        H0 = 71.0
    else:
        H0 = float(H0)

    try:
        float(WM)
    except:
        print "Valid WM value not provided Default WM = 0.27"
        WM = 0.27
    else:
        WM = float(WM)

    try:
        float(WV)
    except:
        print "Valid WV value not provided Default WV = 1.0 - WM - 0.4165/(H0*H0)"
        WV = 1.0 - WM - 0.4165/(H0*H0)
    else:
        WV = float(WV)

    try:
        float(z)
    except:
        print "Valid z value not provided Default z = 3.0"
        sys.exit()
    else:
        z = float(z)
    
    
    WR = 0.        # Omega(radiation)
    WK = 0.        # Omega curvaturve = 1-Omega(total)
    c = 299792.458 # velocity of light in km/sec
    Tyr = 977.8    # coefficent for converting 1/H into Gyr
    DTT = 0.5      # time from z to now in units of 1/H0
    DTT_Gyr = 0.0  # value of DTT in Gyr
    age = 0.5      # age of Universe in units of 1/H0
    age_Gyr = 0.0  # value of age in Gyr
    zage = 0.1     # age of Universe at redshift z in units of 1/H0
    zage_Gyr = 0.0 # value of zage in Gyr
    DCMR = 0.0     # comoving radial distance in units of c/H0
    DCMR_Mpc = 0.0 
    DCMR_Gyr = 0.0
    DA = 0.0       # angular size distance
    DA_Mpc = 0.0
    DA_Gyr = 0.0
    kpc_DA = 0.0
    DL = 0.0       # luminosity distance
    DL_Mpc = 0.0
    DL_Gyr = 0.0   # DL in units of billions of light years
    V_Gpc = 0.0
    a = 1.0        # 1/(1+z), the scale factor of the Universe
    az = 0.5       # 1/(1+z(object))

    h = H0/100.
    WR = 4.165E-5/(h*h)   # includes 3 massless neutrino species, T0 = 2.72528
    WK = 1-WM-WR-WV
    az = 1.0/(1+1.0*z)
    age = 0.
    n=1000         # number of points in integrals
    for i in range(n):
        a = az*(i+0.5)/n
        adot = sqrt(WK+(WM/a)+(WR/(a*a))+(WV*a*a))
        age = age + 1./adot
    
    zage = az*age/n
    zage_Gyr = (Tyr/H0)*zage
    DTT = 0.0
    DCMR = 0.0
    
    # do integral over a=1/(1+z) from az to 1 in n steps, midpoint rule
    for i in range(n):
        a = az+(1-az)*(i+0.5)/n
        adot = sqrt(WK+(WM/a)+(WR/(a*a))+(WV*a*a))
        DTT = DTT + 1./adot
        DCMR = DCMR + 1./(a*adot)

    DTT = (1.-az)*DTT/n
    DCMR = (1.-az)*DCMR/n
    age = DTT+zage
    age_Gyr = age*(Tyr/H0)
    DTT_Gyr = (Tyr/H0)*DTT
    DCMR_Gyr = (Tyr/H0)*DCMR
    DCMR_Mpc = (c/H0)*DCMR
    
    # tangential comoving distance
    
    ratio = 1.00
    x = sqrt(abs(WK))*DCMR
    if x > 0.1:
        if WK > 0:
            ratio =  0.5*(exp(x)-exp(-x))/x 
        else:
            ratio = sin(x)/x
    else:
        y = x*x
        if WK < 0: y = -y
        ratio = 1. + y/6. + y*y/120.
        
    DCMT = ratio*DCMR
    DA = az*DCMT
    DA_Mpc = (c/H0)*DA
    kpc_DA = DA_Mpc/206.264806
    DA_Gyr = (Tyr/H0)*DA
    DL = DA/(az*az)
    DL_Mpc = (c/H0)*DL
    DL_Gyr = (Tyr/H0)*DL

    # comoving volume computation
        
    ratio = 1.00
    x = sqrt(abs(WK))*DCMR
    if x > 0.1:
        if WK > 0:
            ratio = (0.125*(exp(2.*x)-exp(-2.*x))-x/2.)/(x*x*x/3.)
        else:
            ratio = (x/2. - sin(2.*x)/4.)/(x*x*x/3.)
    else:
        y = x*x
        if WK < 0: y = -y
        ratio = 1. + y/5. + (2./105.)*y*y

    VCM = ratio*DCMR*DCMR*DCMR/3.
    V_Gpc = 4.*pi*((0.001*c/H0)**3)*VCM

    Out_Dict = {'age_Gyr':age_Gyr,'zage_Gyr':zage_Gyr, 'DTT_Gyr':DTT_Gyr,'DCMR_Mpc':DCMR_Mpc,'DCMR_Gyr': DCMR_Gyr,'V_Gpc': V_Gpc, 'DA_Mpc':DA_Mpc, 'DA_Gyr':DA_Gyr, 'kpc_DA': kpc_DA, 'DL_Mpc':DL_Mpc, 'DL_Gyr':DL_Gyr, 'DMod':(5*log10(DL_Mpc*1e6)-5)}

    return Out_Dict

        
