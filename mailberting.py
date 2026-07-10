from gmail_auth import get_gmail_service
from email.utils import parseaddr

service = get_gmail_service()


results = service.users().messages().list(
    userId="me",
).execute()

messages = results.get("messages", [])

for msg in messages:

    email = service.users().messages().get(
        userId="me",
        id=msg["id"]
    ).execute()

    subject = "No Subject"
    sender = "Unknown Sender"

    for header in email["payload"]["headers"]:
        if header["name"] == "Subject":
            subject = header["value"]
        elif header["name"] == "From":
            sender = header["value"]

    print("=" * 60)
    print(f"From:    {sender}")
    print(f"Subject: {subject}")
    print("=" * 60)

    choice = input(
        "\n[N]ext  [D]elete  [A]rchive [S] Delete All From Sender [Q]uit: "
    ).lower()

    if choice == "d":
        service.users().messages().delete(
            userId='me',
            id=msg["id"],
        ).execute()
        print("Email has been deleted\n")

    elif choice == "a":
        service.users().messages().modify(
            userId='me',
            id=msg['id'],
            body={"removeLabelIds": ["INBOX"]}

         ).execute()
        print("The email has been archived")

    elif choice == 'q':

        break

    elif choice == "s":
        name, email_address = parseaddr(sender)
        results = service.users().messages().list(
            userId='me',
            q=f'From:{email_address}',
        ).execute()

        messages = results.get('messages', [])

        ids = []

        for msg in messages:
            ids.append(msg["id"])
        
        ## NOTE: Add in sectioning for this area to make reading cmd line easier
        print('=' * 60)
        print(f"Found {len(ids)} emails\nFrom {email_address}")

        delchecksum = input("Confirm delete (Y/N): ").lower()


        if delchecksum == 'y':
            service.users().messages().batchDelete(
                userId='me',
                body={
                    'ids': ids
                }
            ).execute()
            print("Done\n")
            print('=' * 60)




        