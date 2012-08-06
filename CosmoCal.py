#!/usr/bin/env python
import matplotlib
matplotlib.use('TkAgg')

from numpy import arange, sin, pi,log10,max,min,cos,sqrt,exp
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg,NavigationToolbar2TkAgg
from matplotlib.figure import Figure
import cosmocal_nongui as cc
from pprint import pprint

from Tkinter import *
import Pmw, sys
import os


class mywidgets:
	def __init__(self,master):
		frame=Frame(master)
		frame.grid(ipadx=60,ipady=60)
		self.txtfr(frame)
		return

	def txtfr(self,frame):

            #pack everything
                self.lb1 = Label(frame, text="Ho [km/s/Mpc]").grid(row=0,column=0, sticky=E)
                self.lb2 = Label(frame, text="Omega_M").grid(row=1, column=0,sticky=E)
                self.lb3 = Label(frame, text="Redshift z").grid(row=2, column=0, sticky=E)
		self.lb4 = Label(frame, text="Omega_Vac").grid(row=4, column=0, sticky=E)

                self.e1 = Entry(frame,width=8)
		self.e1.insert(0,"71.0")
                self.e2 = Entry(frame,width=8)
		self.e2.insert(0,"0.27")
                self.e3 = Entry(frame,width=8)
		self.e3.insert(0,"3.0")
		self.omvac = StringVar()
		self.omvac.set('0.73')
		self.e4 = Entry(frame,width=8,textvariable=self.omvac)

                self.e1.grid(row=0, column=2, sticky=E)
                self.e2.grid(row=1, column=2, sticky=E)
                self.e3.grid(row=2, column=2, sticky=E)
		self.e4.grid(row=4, column=2, sticky=E)
		self.e4.config(state='disabled')

		self.v = StringVar()
		self.v.set('Flat')
		self.unitype = ['Open', 'Flat', 'General']
		
                for j in range(len(self.unitype)):
			self.ldata = Radiobutton(frame,text=self.unitype[j],variable=self.v,value=self.unitype[j],command=self.getunitype)
			self.ldata.grid(row=3,column=j,sticky=W)

		self.exspace1 = Label(frame,text='---------------------END OF INPUT VARIABLES---------------').grid(row=5,column=0,columnspan=3,rowspan=5,sticky=E+W)
                self.cal = Button(frame, text='Calculate', command=self.cosmocalc)
                self.cal.grid(column=0, row=12,rowspan=2, columnspan=1, sticky=W)

		#self.q = Button(frame, text='Quit', command=frame.quit)
                #self.q.grid(column=1, row=5, sticky=W)

		self.Line1 = StringVar()
		self.Line1.set('For H_o = ' + '%1.1f' % 71.0 + ', Omega_M = ' + '%1.2f' % 0.27 + ', Omega_vac = '
		'%1.2f' % 0.73 + ', z = ' + '%1.3f' % 3.0)
		self.l1 = Label(frame,textvariable=self.Line1).grid(row=10, column=0,columnspan=3,sticky=W)

		self.Line2 = StringVar()
		self.Line2.set('It is now ' + '%1.3f' % 13.666 + ' Gyr since the Big Bang.')
		self.l1 = Label(frame,textvariable=self.Line2).grid(row=14, column=0,columnspan=3,sticky=W)

		self.Line3 = StringVar()
		self.Line3.set('The age at redshift z was ' + '%1.3f' % 2.190 + ' Gyr.')
		self.l1 = Label(frame,textvariable=self.Line3).grid(row=15, column=0,columnspan=3,sticky=W)

		self.Line4 = StringVar()
		self.Line4.set('The light travel time was ' + '%1.3f' % 11.476  + ' Gyr.')
		self.l1 = Label(frame,textvariable=self.Line4).grid(row=16, column=0,columnspan=3,sticky=W)

		self.Line5 = StringVar()
		self.Line5.set('The comoving radial distance, which goes into Hubbles law, is %1.2f' % 6460.63 + ' Mpc or ' + '%1.2f' % 21.07 + ' Gly.')
		self.l1 = Label(frame,textvariable=self.Line5).grid(row=17, column=0,columnspan=3,sticky=W)

		self.Line6 = StringVar()
		self.Line6.set('The comoving volume within redshift z is ' + '%1.2f' % 1129.52 + ' Gpc^3.')
		self.l1 = Label(frame,textvariable=self.Line6).grid(row=18, column=0,columnspan=3,sticky=W)

		self.Line7 = StringVar()
		self.Line7.set('The angular size distance D_A is ' + '%1.2f' % 1615.10 + ' Mpc or %1.2f' % 5.27 + ' Gly.')
		self.l1 = Label(frame,textvariable=self.Line7).grid(row=19, column=0,columnspan=3,sticky=W)

		self.Line8 = StringVar()
		self.Line8.set('This gives a scale of ' + '%.2f' % 7.83 + ' kpc/".')
		self.l1 = Label(frame,textvariable=self.Line8).grid(row=20, column=0,columnspan=3,sticky=W)

		self.Line9 = StringVar()
		self.Line9.set('The luminosity distance D_L is ' + '%1.2f' % 25841.67 + ' Mpc or ' + '%1.2f' % 84.28 + ' Gly.')
		self.l1 = Label(frame,textvariable=self.Line9).grid(row=21, column=0,columnspan=3,sticky=W)

		self.Line10 = StringVar()
		self.Line10.set('The distance modulus, m-M, is '+'%1.2f' % (5*log10(25841.7*1e6)-5))
		self.l1 = Label(frame,textvariable=self.Line10).grid(row=22, column=0,columnspan=3,sticky=W)
		

		return


	def getunitype(self):
		try:
			self.v.get() != "None"
		except KeyError:
			print "Default Univerise Type is Open and thus Omega_vac = 0"
		else:
			self.myuni=self.v.get()
			if self.myuni == 'Flat':
				if len(self.e2.get().strip().split()) == 1:
					self.OmegaM = self.e2.get().strip().split()[0]
					try:
						float(self.OmegaM)
					except AttributeError as a:
						print "Attribute error : Please enter a valid value of OmegaM < 1.0 "
					except ValueError:
						print "For the choice of Flat Universe, Omega_Vac = 1.0 - Omega_M. Please Enter a valid value for Omega_M"
						raise
					else:
						dum = 1.0 - float(self.OmegaM)
						self.omvac.set(str(dum))
				else:
					print "For the choice of Flat Universe, Omega_Vac = 1.0 - Omega_M. Please enter a valid value for Omega_M"
			
			elif self.myuni == 'Open':
				self.omvac.set('0')
				self.e4.config(state='disabled')
			else:
				self.e4.config(state='normal')

	def getinputs(self):
			# Get Input Values
		if len(self.e1.get().strip().split()) == 1:
			self.H0 = self.e1.get().strip().split()[0]
			try:
				float(self.H0)
			except AttributeError as a:
				print "Attribute error : Please enter a valid float value of H0 "
			except ValueError:
				print "Please Enter a valid value for H0"
				raise
			else:
				H0 = float(self.H0)
		else:
			print "Please enter a valid value for H0"


		if len(self.e3.get().strip().split()) == 1:
			self.redshiftz = self.e3.get().strip().split()[0]
			try:
				float(self.redshiftz)
			except AttributeError as a:
				print "Attribute error : Please enter a valid float value of z "
			except ValueError:
				print "Please Enter a valid value for z"
				raise
			else:
				z = float(self.redshiftz)
		else:
			print "Please enter a valid value for z"


		if len(self.e2.get().strip().split()) == 1:
			self.OmegaM = self.e2.get().strip().split()[0]
			try:
				float(self.OmegaM)
			except AttributeError as a:
				print "Attribute error : Please enter a valid value of OmegaM < 1.0 "
			except ValueError:
				print "For the choice of Flat Universe, Omega_Vac = 1.0 - Omega_M. Please Enter a valid value for Omega_M"
				raise
			else:
				WM = float(self.OmegaM)
		else:
			print "Please enter a valid value for OmegaM"
		
		WV = float(self.omvac.get())
		
		self.Line1.set('For H_o = ' + '%1.1f' % H0 + ', Omega_M = ' + '%1.2f' % WM + ', Omega_vac = '
		'%1.2f' % WV + ', z = ' + '%1.3f' % z)

		return H0, z, WM, WV
		
				
	def cosmocalc(self):
		self.getunitype()
		H0, z, WM, WV = self.getinputs()
		Out_Dict=cc.CC_nongui(z=z,H0=H0, WM=WM,WV=WV)
		self.Line2.set('It is now ' + '%1.3f' % Out_Dict['age_Gyr'] + ' Gyr since the Big Bang.')
		self.Line3.set('The age at redshift z was ' + '%1.3f' % Out_Dict['zage_Gyr'] + ' Gyr.')
		self.Line4.set('The light travel time was ' + '%1.3f' % Out_Dict['DTT_Gyr'] + ' Gyr.')
		
		self.Line5.set('The comoving radial distance, which goes into Hubbles law, is %1.2f' % Out_Dict['DCMR_Mpc'] + ' Mpc or ' + '%1.2f' % Out_Dict['DCMR_Gyr'] + ' Gly.')
		self.Line6.set('The comoving volume within redshift z is ' + '%1.2f' % Out_Dict['V_Gpc'] + ' Gpc^3.')
		self.Line7.set('The angular size distance D_A is ' + '%1.2f' % Out_Dict['DA_Mpc'] + ' Mpc or %1.2f' % Out_Dict['DA_Gyr'] + ' Gly.')
		self.Line8.set('This gives a scale of ' + '%.2f' % Out_Dict['kpc_DA'] + ' kpc/".')
		self.Line9.set('The luminosity distance D_L is ' + '%1.2f' % Out_Dict['DL_Mpc'] + ' Mpc or ' + '%1.2f' % Out_Dict['DL_Gyr'] + ' Gly.')
		self.Line10.set('The distance modulus, m-M, is '+'%1.2f' % Out_Dict['DMod'])
	
	
		
			
				
if __name__ == "__main__":
	
	if len(sys.argv) < 2:
		print " SYNTAX: python ComsoCal.py <flag>"
		print " The flag can be either of these two:"
		print " <flag> = -gui : This invoked the Graphic User Interface Option [Requires Python Tkinter]"
		print " <flag> = -ngui <z> <H0> <WM> <WV> : This invokes the normal Python Interface "
		sys.exit()
	elif sys.argv[1] == '-gui':
		root=Tk()
		app=mywidgets(root)
		root.title("Cosmology Calculator")
		root.mainloop()
	elif sys.argv[1] == '-ngui':
		if len(sys.argv) < 3:
			print "With -ngui flag the syntax is"
			print "python CosmoCal -ngui z (H0 WM WV) "
			print "REQUIRED ARGS :"
			print "              z - Redshift"
			print "OPTIONAL ARGS :"
			print "              H0 - Hubble Constant in km/s/Mpc [ DEFAULT = 71.0 km/s/Mpc]"
			print "              WM - Omega Matter [DEFAULT = 0.27]"
	                print "              WV - Omega Vaccum. [DEFAULT = 1.0 - WM - 0.4165/(H0*H0)]"
		elif len(sys.argv) == 3:
			Out_Dict=cc.CC_nongui(z=sys.argv[2], H0=None, WM=None, WV=None)
			pprint(Out_Dict)
		elif len(sys.argv) == 4:
			Out_Dict=cc.CC_nongui(z=sys.argv[2], H0=sys.argv[3], WM=None, WV=None)
			pprint(Out_Dict)
		elif len(sys.argv) == 5: 
			Out_Dict=cc.CC_nongui(z=sys.argv[2], H0=sys.argv[3], WM=sys.argv[4], WV=None)
			pprint(Out_Dict)
		elif len(sys.argv) == 6:
			Out_Dict=cc.CC_nongui(z=sys.argv[2], H0=sys.argv[3], WM=sys.argv[4], WV=sys.argv[5])
			pprint(Out_Dict)
		else:
			print "Too Many agruments"
			print "With -ngui flag the syntax is"
			print "python CosmoCal -ngui z (H0 WM WV) "
			print "REQUIRED ARGS :"
			print "              z - Redshift"
			print "OPTIONAL ARGS :"
			print "              H0 - Hubble Constant in km/s/Mpc [ DEFAULT = 71.0 km/s/Mpc]"
			print "              WM - Omega Matter [DEFAULT = 0.27]"
	                print "              WV - Omega Vaccum. [DEFAULT = 1.0 - WM - 0.4165/(H0*H0)]"
			sys.exit()
	else:
		print " SYNTAX: python ComsoCal.py <flag>"
		print " The flag can be either of these two:"
		print " <flag> = -gui : This invoked the Graphic User Interface Option [Requires Python Tkinter]"
		print " <flag> = -ngui <z> <H0> <WM> <WV> : This invokes the normal Python Interface "
		sys.exit()
		
		
	
		
