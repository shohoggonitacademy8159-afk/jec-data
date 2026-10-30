import json,glob,os,sys
base=sys.argv[1]  # dir containing routines/ and notes/ exports
def load(d):
    out=[]
    for f in sorted(glob.glob(f'{base}/{d}/*.json')):
        j=json.load(open(f)); x=j.get('data',j) if isinstance(j,dict) and 'data' in j and 'id' in j else j
        x=dict(x); x['id']=os.path.basename(f)[:-5]; out.append(x)
    return out
json.dump({"routines":load('routines'),"notes":load('notes')},open('sync.json','w'),ensure_ascii=False,separators=(',',':'))
print('ok')
