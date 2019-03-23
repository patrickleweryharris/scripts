(*using terms from application "Mail"
    on perform mail action with messages theMessages for rule theRule*)

set MainFolder to "Dropbox" -- After the current users home dir
set subFolder to "mail"

-- The folder to save the attachments in (must already exist)
tell application "Finder" to set attachmentsFolder to ((path to home folder as text) & MainFolder & ":" & subFolder) as text

tell application "Mail"
    set theMessages to the selected messages of the front message viewer
    --set theMessage to first item of theMessages

    repeat with eachMessage in theMessages
        set theAddress to extract address from sender of eachMessage

        if (count of (eachMessage's mail attachments)) > 0 then
            try
                tell application "Finder"
                    if not (exists folder theAddress of folder attachmentsFolder) then
                        make new folder at attachmentsFolder with properties {name:theAddress}
                    end if
                end tell
                -- Save the attachment
                repeat with theAttachment in eachMessage's mail attachments

                    set originalName to name of theAttachment
                    set savePath to attachmentsFolder & ":" & theAddress & ":" & originalName

                    tell application "Finder"
                        if (exists file originalName of folder theAddress of folder attachmentsFolder) then
                            set savePath to attachmentsFolder & ":" & theAddress & ":" & originalName
                        end if
                    end tell
                    try
                        save theAttachment in file (savePath)
                    end try
                end repeat
            on error error_message number error_number

            end try
        end if
    end repeat

end tell
(*end perform mail action with messages
end using terms from*)
