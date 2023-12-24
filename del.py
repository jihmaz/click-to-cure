from replit import db
if 'assistant_id' in db:
  del db['assistant_id']
  print("deleted")
else:
  print("not found")
  
