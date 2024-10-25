import os

def load_cfg(path: str) -> dict | None:
    if os.path.exists(path):
        with open(path, 'rt') as f:
            # reformat list to exclude comments starting with # and process newlines
            data = f.read().split('\n')
            _data = []

            i = 0
            while i < len(data):
                line = data[i].strip()
                if not line.startswith('#') or line == '':
                    if not line.endswith('|'):
                        _data.append(line)
                    else:
                        _data.append("")
                        # read to last new-line
                        while data[i].endswith('|'):
                            _line = data[i].strip()
                            _data[-1] += _line[:-1]
                            i += 1
                        
                        # get next line since it doesnt end with |
                        _line = data[i].strip()
                        _data[-1] += _line

                i += 1

            while '' in _data:
                _data.remove('')
            
            # convert list into dict
            conf = {}
            for kvp in _data:
                keyval = kvp.split('=')
                _val = keyval[1]

                # convert type if necessary
                if _val == '#bool true':
                    _val = True
                elif _val == '#bool false':
                    _val = False
                elif _val == '#nil':
                    _val = None
                elif _val.startswith('#num'):
                    _val = int(_val.replace('#num ', ''))
                
                conf.update({f"{keyval[0]}": _val})

            return conf

    else:
        return None