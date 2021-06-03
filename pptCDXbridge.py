from AppKit import NSPasteboard, NSRange, NSData, NSMakeRange, NSNotFound

pb = NSPasteboard.generalPasteboard()
pbItems = pb.pasteboardItems()
types = pbItems[0].types()
count = types.count()

### Binary header for CDX blob, used as search term
sterm = NSData.alloc().initWithBytes_length_('VjCD0100',8)

### Get binary chemdraw data, throw error if not found

for i in range(0,count):
    ret = pb.dataForType_(types[i])
    maxrng = NSMakeRange(0, ret.length() - 1)
    datastart = ret.rangeOfData_options_range_(sterm,0,maxrng)

    ### check to see if search term is successful

    if(datastart.location != NSNotFound):
        break

### error checking, if the binary header is not found, just bomb out and don't touch the pasteboard
if(datastart.location == NSNotFound):
    exit()

### range of valid binary CDX data in pasteboard item
### don't need end of data, ChemDraw reads in from binary data and ends at pair of 0 bytes
datarng = NSMakeRange(datastart.location, ret.length() - datastart.location)

### pull subdata range from main pasteboard item
outdata = ret.subdataWithRange_(datarng)

### binary CDX data obtained; putting back on clipboard in format recognizable to ChemDraw
perkinelmerType = u'com.perkinelmer.chemdraw.cdx-clipboard'
pb.clearContents()
pb.setData_forType_(outdata, perkinelmerType)

### done
