#!/usr/bin/python3.4
# Written by Anirudh Anand (lucif3r) : email - anirudh@anirudhanand.com
# This program will help to decrypt cipher text to plain text if you have
# more than 1 cipher text encrypted with same Modulus (N) but different
# exponents. We use extended Euclideangm Algorithm to achieve this.

import gmpy2


class RSAModuli:
    def __init__(self):
        self.a = 0
        self.b = 0
        self.m = 0
        self.i = 0

    def gcd(self, num1, num2):
        """
           This function os used to find the GCD of 2 numbers.
           :param num1:
           :param num2:
           :return:
           """
        if num1 < num2:
            num1, num2 = num2, num1
        while num2 != 0:
            num1, num2 = num2, num1 % num2
        return num1

    def extended_euclidean(self, e1, e2):
        """
           The value a is the modular multiplicative inverse of e1 and e2.
           b is calculated from the eqn: (e1*a) + (e2*b) = gcd(e1, e2)
           :param e1: exponent 1
           :param e2: exponent 2
           """
        self.a = gmpy2.invert(e1, e2)
        self.b = (float(self.gcd(e1, e2)-(self.a*e1)))/float(e2)

    def modular_inverse(self, c1, c2, N):
        """
           i is the modular multiplicative inverse of c2 and N.
           i^-b is equal to c2^b. So if the value of b is -ve, we
           have to find out i and then do i^-b.
           Final plain text is given by m = (c1^a) * (i^-b) %N
           :param c1: cipher text 1
           :param c2: cipher text 2
           :param N: Modulus
           """
        i = gmpy2.invert(c2, N)
        mx = pow(c1, self.a, N)
        my = pow(i, int(-self.b), N)
        self.m = mx * my % N
    def print_value(self):
        print("Plain Text: ", self.m)


def main():
    c = RSAModuli()
    N = 25458200992030509733740123651871827168179694737564741891817013763410533831135578900317404987414083347009443171337016804117994550747038777609425522146275786823385218489896468142658492353321920860029284041857237273061376882168336089921980034356731735024837853873907395117925738744950932927683784527829300499629044776530663084875991411120648155572219472426590747952180037566734905079883718263249789131313731453855593891997376222635496337534679814697188141565730768050813250191975439504290665602928172394124501396491438097237093345376202142503439944034846839870643057174427346860377971316738504003909365471892007511334129
    c1 = 19074438470072195427966520314234457847008607427606084653244579403273587717215359437848959151287968653813774451872243596539852961112790372328452176435310940366312355444995843216994547119328105950997441430508803799696108202263077660206667410037895728991246260073976495701990246589717169815787627260333746927676703415397948299928151669728670970891826725671026488571268125861689964688240713660432174319415041362820791863237794347031803574182264640071528640168842529541888996148513070006266317160300336104047046565614107490019016833308549850299600989228190163831642944507973854553499903518264459385900876967183424703346566
    c2 = 17147905252678781157626731164660022679389951402035723790864177724472811805536492684462105274963820085525923148442586230016346022360533813239980197823588694113614328942373594914090007235565086360669401527248700861049825216638433673668883632064731716051799766945737234155585371938261291032941617911654796216200373195747432329591657679097825944679339369336644061159658436125778459206858632826310294115276289447751653250081978372776233383658861171699105292372718533428579168281346425439711770636421673291051002416067073005799659684303566722822458673952580001750804105442227754799536262315625088085767607467446614116889593
    e1 = 22255763231110249841946619835451544743470788953822278626567823902873888725104180401047359514978597528256727783972109939326623409435352523707077685530090905587264556011558283062584063790610407522064244766804545192800000203519996147931257064951519705687708204481851413899370853107413015511963924826116255617048471033727588623329910848658324118717242497443676679226618430348230146770121025920211016222285978389380202889753020268614144716241830764562717015776308425373054119742788593926393822433887270639369774139542440755201713961244129409678232953199572105700556795757766046717275157050721726002297647024020428198870290
    e2 = 23295046285127774160603234291301851851887586336491694096135804083341667982196486623010787985772884401302006627480506928365762168889259124596656609547973623161028214128429382170008181185180817200188852310143707964673736007253037970626819969310508212349854949150027746456459910448148518206090222496335254237639366458956363901115228820515207791697374943745570543635069929211464017776268424656451494147324386568859163866168248303418756480467046005765139197217754018136577337642795325944222997798231137981998354508181409469926672642302422740898720854693114056342834487668008885129303781190655860432910789997267090661459286
    c.extended_euclidean(e1, e2)
    c.modular_inverse(c1, c2, N)
    c.print_value()


if __name__ == '__main__':
    main()