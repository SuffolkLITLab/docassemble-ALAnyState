import advertise_capabilities from docassemble.ALWeaver.custom_values

if not __name__ == '__main__' and not os.environ.get('ISUNITTEST'):
  advertise_capabilities()