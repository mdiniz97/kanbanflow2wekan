import os
from dotenv import load_dotenv
from kanbanflow2wekan import k2w

load_dotenv()

print('kanbanflow2wekan | by: @mdiniz97\n\n')

migration = k2w(
  os.getenv('WEKAN_URL'),
  os.getenv('WEKAN_USER'),
  os.getenv('WEKAN_PASSWORD'),
  os.path.join(os.getcwd(), 'kanbanflow'), # path to kanbanflow dump's folder
  os.getenv('KANBANFLOW_USER'),
  os.getenv('KANBANFLOW_PASSWORD'),
  kf_download_attachments=True,
)

migration.migrate()