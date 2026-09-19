from hospital import Hospital
from atencion import Atencion, AtencionFarmacia, AtencionMedica
from paciente import Paciente


def main():
    nombre = "hopitivity wonder"
    hospital = Hospital(nombre)
    archfarm = open("atenciones_farmacia.csv")
    archmedi = open("atenciones_medicas.csv")
    archpaci = open("pacientes.csv")
    b1 =False
    b2 =False
    b3 =False 

    pacientes = []

    for linea in archpaci.readlines():
        if not b1:
            b1 = True
            pass
        else:
            dato = linea.split(",")
            codigo = int(dato[0])
            nombre = dato[1]
            sintoma = int(dato[2])
            habitual = dato[3].strip().lower() == "true"
            paciente = Paciente(nombre, sintoma, habitual)

            archmedi.seek(0)
            b3 = False

            for l in archmedi.readlines():
                if not b3: 
                    b3 = True 
                    continue      
                           
                d = l.split(",")
                if int(d[0]) == codigo:
                    codigo = int(d[0])
                    tipo = int(d[1])
                    importe = float(d[2])
                    atencion = AtencionMedica(codigo, tipo, paciente, importe)
                    hospital.addAtencion(atencion)
    for l in archfarm.readlines():
        if not b2: 
            b2 = True 
            continue 
    
        d = l.split(",")
        codigo = int(d[0])                
        tipo = int(d[1])
        importe_total = float(d[2])
        cupon = float(d[3])
        atencion = AtencionFarmacia(codigo, tipo, importe_total, cupon)
        hospital.addAtencion(atencion)

    print(hospital.__str__())
    print(hospital.importe_total_atencion_consulta())
    print(hospital.importe_promedio_atenciones(1000, 100000))
    print(hospital.codigo_primera_atencion_habitual())

if __name__ == "__main__":
    main()