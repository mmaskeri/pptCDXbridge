# pptCDXbridge

Generation and editing of slide presentations containing ChemDraw schemes between Windows and macOS is occasionally stymied by the roundtrip editing problem. For PowerPoint presentations created and edited on Windows, and correspondingly on macOS, roundtrip editing is easily accomplished using the clipboard. Presentations made on Windows and opened on macOS, however, can present the frustrating scenario in which a scheme copied from PowerPoint into ChemDraw produces an uneditable PDF graphic.

In this instance PowerPoint (like Keynote, see github.com/mmaskeri/keyClip) strips the chemical metadata from the PDF image of the scheme and serves it to the pasteboard as an NSPasteboardType that is unrecognizable by ChemDraw. pptCDXbridge searches the pasteboard for CDX data and re-serves it to the pasteboard in a type that ChemDraw can use. A user can then simply paste a fully-editable scheme into ChemDraw.

pptCDXbridge consists of two components:
- **pptCDXbridge.py:** general tool that searches the pasteboard for binary CDX data and returns it to the pasteboard as an NSData object with type `com.perkinelmer.chemdraw.cdx-clipboard`
- **pptCDXbridge_workflow.workflow:** macOS service that copies a selected (ungrouped) PowerPoint object to the pasteboard and runs pptCDXbridge.py

## Setup
pptCDXbridge.py can be run on its own as long as the pasteboard has been populated with the requisite data. The service provides a compact harness and takes care of copying.
1. Add pptCDXbridge.py to `~/Library/Scripts`, creating the `Scripts` directory if necessary
2. Add pptCDXbridge_workflow.workflow to `~/Library/Services`
3. Add keyboard shortcut to pptCDXbridge_workflow from System Preferences:
   - Open System Preferences > Keyboard > Shortcuts > Services
   - Under General, check the box next to pptCDXbridge_workflow
   - Click "none" and press key combination for shortcut. Suggestion is option-⌘-c
     - This shortcut must not collide with any system/PowerPoint shortcuts

## Usage
Ungroup ChemDraw object in PowerPoint if necessary. Select object, then input keyboard shortcut established in Setup step 3 above. Script will run, briefly displaying small rotating gear in menu bar. Paste as normal into ChemDraw (⌘-v).

If pptCDXbridge does not find any binary CDX data on the pasteboard, the pasteboard will be unchanged.

(c) 2021 M. Maskeri, see LICENSE (MIT)
