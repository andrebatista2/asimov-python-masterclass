import sys
from streamlit.web import cli as stcli

sys.argv = ['streamlit', 'run', 'application.py', '--server.port=8001']
sys.exit(stcli.main())
