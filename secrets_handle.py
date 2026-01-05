" ************************************************************************************************ "
# This file contains the main function for torsion points computation and secret isogeny recovery. # 
" ************************************************************************************************ "

from sage.all import *
from isogeny_computations.torsion_handle import Sharing_Data_Computation, Isogeny_Recomputation
from isogeny_computations.goodprime_parameters_generation import read_params_SIKE
import argparse

if __name__=="__main__":
	fprime_params=read_params_SIKE('isogeny_computations/GoodPrime_SharingPath_Parameters.txt')
	parser = argparse.ArgumentParser()

	# To precompute the public and private data given to the dealer
	parser.add_argument("--Dealer_Data",action="store_true")
	# To run the overall process of isogeny recomputation
	parser.add_argument("--Sharing_and_Recovering",action="store_true")

	# Parameter
	parser.add_argument("-p")
	args = parser.parse_args()

	if args.Dealer_Data:
		x=args.p
		print("\n We work with the prime number {}=(2^{})x(3^{})-1\n".format(x,fprime_params[x]['e2'],fprime_params[x]['e3']))
		priv_torsions,imgA,imgB,EAB=Sharing_Data_Computation(fprime_params[x])

	elif args.Sharing_and_Recovering:
		x=args.p
		print("\n We work with the prime number {}=(2^{})x(3^{})-1\n".format(x,fprime_params[x]['e2'],fprime_params[x]['e3']))
		priv_torsions,imgA,imgB,EAB=Sharing_Data_Computation(fprime_params[x])
		print("\n")
		Iso_secret = Isogeny_Recomputation(fprime_params[x],priv_torsions,imgA,imgB,EAB)
