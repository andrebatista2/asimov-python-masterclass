import sys
from streamlit.web import cli as stcli

sys.argv = ['streamlit', 'run', 'index.py', '--server.port=8001']
sys.exit(stcli.main())
