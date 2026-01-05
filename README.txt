The goal of this library is to implement functions that account for the majority
of the computational cost in the secret sharing scheme introduced in our document
"Sharing the Path: A Threshold Scheme from Isogenies and Error Correcting Codes".
We aim to compare this cost with the majority of the runtime of the seminal isogeny-based 
threshold scheme proposed by De Feo and Meyer [1]. Specifically, this comparison is intended 
to highlight the efficiency of our approach relative to the first isogeny-based threshold 
scheme, in particular, the one based on class group action combined with Shamir’s secret sharing.

The cost of the algorithm in [1] is dominated by a class group action computation
of the form [s]E, where s is a Shamir secret and E is an elliptic curve (see [4, Algorithm 3, Line 5]).
On the other hand, Line 23 of [4, Algorithm 2], which involves isogeny recomputation,
represents the main computational cost of our scheme. Therefore, the comparison focuses
on the implementation of the core functions for isogenies that can be found in the files 
        "secrets_handle.py" and "isogeny_computations/torsion handle.py". 
As explained in the manuscript, other sub-processes—such as encoding and bit concatenation—are negligible 
in terms of computational cost. Nevertheless, we implemented the prerequisite functions and provided a 
blueprint for integrating these sub-processes with isogeny computations during the secret sharing and recovery 
phases. The prerequisite functions for finite field parameters, bit and symbol operations, encoding parameters, 
and related tasks can be found in the files 
        "schemepara.py" and "sharingtools.py".

This library relies on functions developed in Dartois's library [2], which itself heavily depends on the 
computations presented in [3]. We adapt their packages to the context of our threshold scheme, where key 
exchange between two parties is not required, and the torsion points are treated as secret parameters.

Benchmarking
The values presented at row 5 of our comparison table [4, Table 2] are the result of multiple executions 
of the main function in the file secrets_handle.py. We took the average values after running the script 
several times.  The idea is to compare the bulk of the computational cost of our algorithm with the running 
time of the class group computation, which dominates the cost of the algorithms in De Feo and Meyer’s scheme [1]. 
The performance of their scheme can be inferred from the CSI-FiSh paper, and we directly reported the bulk of 
this running time in our manuscript [4, Table 2, Row 4]. For more details, see [4, Section 6].


How to Run the Code?
Before running secrets_handle.py, first run torsion_handle.py, which defines the secret torsion points
provided to the dealer.

    > run torsion_handle.py
        This file is located in the isogeny_computations directory.

    > run secrets_handle.py --Sharing_and_Recovering -p=pX
        This file is located in the main directory.

In the argument -p=pX, the value X represents the bit-size of the prime and must be one of the following:
{p128, p288, p434, p503, p610, p640, p751}. If you only want to display the public data and the private 
elements given to the dealer, modify command (2) as follows:

    > run secrets_handle.py --Dealer_Data -p=pX
 

[1] L. De Feo, M. Meyer: Threshold schemes from isogeny assumptions. In: Kiayias, A.,652
Kohlweiss, M., Wallden, P., Zikas, V. (eds.) PKC 2020. LNCS, vol. 12111, pp. 187–212.653
Springer, Cham (2020). https://doi.org/10.1007/978-3-030-45388-6_7

[2] P. Dartois: Fast computation of 2-isogenies in dimension 4 and cryptographic628
applications Cryptology ePrint Archive, Paper 2024/1180, 2024, https://eprint.iacr.org/2024/1180

[3] Pierrick Dartois, Luciano Maino, Giacomo Pope and Damien Robert: An Algorithmic Approach 
to (2,2)-isogenies in the Theta Model and Applications to Isogeny-based Cryptography, In Advances 
in Cryptology – ASIACRYPT 2024. https://eprint.iacr.org/2023/1747.

[4] Our submitted manuscrit: Sharing the Path: A Threshold Scheme from Isogenies and Error-Correcting Codes
