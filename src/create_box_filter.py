import numpy



l0 = 6000
lf = 6500
flat = 100 

if l0-flat>0:
    lf0 = l0-flat
else:
    lf0 = 0

lff = lf + flat

before = numpy.linspace(lf0, l0-1, l0-lf0)
center = numpy.linspace(l0, lf, lf-l0)
after = numpy.linspace(lf+1, lff, lff-lf)

before_flux = numpy.zeros(len(before)) 
center_flux = numpy.ones(len(center))
after_flux = numpy.zeros(len(after))

wave = list(before) + list(center) + list(after)
throughput = list(before_flux) + list(center_flux) + list(after_flux)


##save
numpy.savetxt('box_%s_%s.ascii'%(l0, lf), numpy.array([numpy.array(wave), numpy.array(throughput)]).T)




