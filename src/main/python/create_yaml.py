import yaml
import app

app.testing()
dict_file = {
             'pullPolicy': 'Always',
             'cpuLimit': app.d1,
             'cpuRequest': app.d2,
             'image': app.d3,
             'memoryLimit': app.d4,
             'memoryRequest': app.d5,
             'replicaCount': app.d6,
             'serviceport': app.d7,
             'servicetype': app.d8,
             }
with open(r'helm/flaskapp/values.yaml', 'w') as file:
    documents = yaml.dump(dict_file, file)
