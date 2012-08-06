NAME : pyCOSMOCAL 

TASK : Ned Wright Cosmology Calculator [http://www.astro.ucla.edu/~wright/CosmoCalc.html] with Graphic User Interface

AUTHORS : Bhargav Vaidya [University of Leeds]

DESCRIPTION:
The code is completely written using the Python Language. 
The original python code for the non gui version is adapted from CC.py by
James Schombert. Further the GUI is developed with the Tkinter Interface.

FEATURES: 
The GUI environment provides a similar work flow structure like the
Java Script HMTL CosmoCalc developed by Wright 2006. 

QUICK START :
After sucessful installation and careful inclusion of required path in the
PATH variable, one would be able to invole the command ./CosmoCal.py.
If no flags are provided the command would by default show the required
syntax.
SYNTAX: python ComsoCal.py <flag>
The flag can be either of these two:
<flag> = -gui : This invoked the Graphic User Interface Option [Requires Python Tkinter]
<flag> = -ngui z (H0 WM WV) : This invokes the normal Python Interface 

Thus, in order to start the Calculator in GUI form invoke the command
vaidya@home> ./CosmoCal.py -gui

This will prompt a Tkinter Window which has similar functionality of the
JavaScript Calculator.

In order to work in Non GUI format, there are basically two methods.
1. Command Line Option:
vaidya@home> ./CosmoCal.py -ngui z (H0, WM, WV)

If no arguments are provided after the '-ngui' flag the resultant output will
remind the user the correct syntax i.e.

With -ngui flag the syntax is
python CosmoCal -ngui z (H0 WM WV) 
REQUIRED ARGS :
              z - Redshift
OPTIONAL ARGS :
              H0 - Hubble Constant in km/s/Mpc [ DEFAULT = 71.0 km/s/Mpc]
              WM - Omega Matter [DEFAULT = 0.27]
              WV - Omega Vaccum. [DEFAULT = 1.0 - WM - 0.4165/(H0*H0)]

As mentioned the value of redshift is essential else the code will not
function and prompt for a valid value of z. The other quantities are optional
if these values are not provided the code assumes default values as indicated
above.

2.Using python (or IPython) prompt:
One can also use the Python (or IPython) prompt in the manner described below,

vaidya@home> python
Enthought Python Distribution -- www.enthought.com
Version: 7.2-1 (64-bit)

Python 2.7.2 |EPD 7.2-1 (64-bit)| (default, Jul 27 2011, 14:50:45) 
[GCC 4.0.1 (Apple Inc. build 5493)] on darwin
Type "packages", "demo" or "enthought" for more information.
>>> import cosmocal_nongui as cc
>>> Out_Dict = cc.CC_nongui(3.0,71.0,0.27,0.73)
>>> from pprint import pprint
>>> pprint(Out_Dict)
{'DA_Gyr': 5.2678075619641413,
 'DA_Mpc': 1615.1042925672091,
 'DCMR_Gyr': 21.071909562803281,
 'DCMR_Mpc': 6460.6254475214764,
 'DL_Gyr': 84.284920991426262,
 'DL_Mpc': 25841.668681075345,
 'DMod': 47.061602770219039,
 'DTT_Gyr': 11.47608214682462,
 'V_Gpc': 1129.5240939432965,
 'age_Gyr': 13.665696769001471,
 'kpc_DA': 7.8302465839335147,
 'zage_Gyr': 2.1896146221768507}
>>> 
Thus the output is stored in form of a Dictionary with keys described below,
DA : Angular Distance [_Gyr in Giga Year, _Mpc in Mega Parsec, _kpc in
kiloparsec]
DCMR : Comoving radial distance [_Gyr in Giga Year, _Mpc in Mega Parsec] 
DL : Luminosity Distance [_Gyr in Giga Year, _Mpc in Mega Parsec]
DMod : Distance modulus
DTT : Time from z to now
V_Gpc : Comoving volume within redshift in Gpc3.
age_Gyr: Age of Universe in Gyr
zage_Gyr: Age of Universe at redshift z in Gyr




