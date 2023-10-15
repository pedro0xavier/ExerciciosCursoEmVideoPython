metros = float(input('Digite um valor em metros para fazer a conversão '))
centimts = metros * 100
mm = metros * 1000
km = metros / 1000
hm = metros / 100
dam = metros /10
dm = metros * 10
print (' {:.1f}m corresponde a {:.0f}cm e {:.0f}mm '.format(metros,centimts,mm),end = '')
print ('além de corresponder a {}hm, {}dam e {}dm'.format(hm,dam,dm))
