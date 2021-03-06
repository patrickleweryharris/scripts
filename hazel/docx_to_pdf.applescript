set _document to theFile
-- Open a docx document in pages and auto export to PDF
tell application "Finder"

  set _directory to get container of file _document
  set _documentName to name of _document
  -- Figure out document name without sextension
  if _documentName ends with ".docx.docx" then ¬
    set _documentName to text 1 thru -6 of _documentName
  if _documentName ends with ".docx" then ¬
    set _documentName to text 1 thru -6 of _documentName


  set _PDFName to _documentName & ".pdf"
  set _location to (_directory as string) & _PDFName
end tell

tell application "Pages"
  activate
  open _document
  with timeout of 1200 seconds
    -- Export as PDF with _PDFName
    export front document to file _location as PDF
  end timeout

  close front document
end tell
