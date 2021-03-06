set _document to theFile
-- Open xlsx doc in Numbers, export it to PDF
tell application "Finder"
  set _directory to get container of file _document
  set _documentName to name of _document
  -- Find out filename without extension
  if _documentName ends with ".xlsx.xlsx" then ¬
    set _documentName to text 1 thru -6 of _documentName
  
  if _documentName ends with ".xlsx" then ¬
    set _documentName to text 1 thru -6 of _documentName
  
  set _PDFName to _documentName & ".pdf"
  set _location to (_directory as string) & _PDFName
end tell

tell application "Numbers"
  activate
  open _document
  -- Export to PDF
  with timeout of 1200 seconds
    export front document to file _location as PDF
  end timeout
  
  close front document
end tell
