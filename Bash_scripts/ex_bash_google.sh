# echo cada pid de todos los pids de chrome
for pid in $(pidof chrome); do echo "$pid"; done


# cambiando la prioridad de cada pid de chrome a 19
for pid in $(pidof chrome); do renice 19 $pid; done


# Dentro del bucle for, queremos enviar la señal cont y luego esperar hasta que finalice el proceso.
# Desafortunadamente, no hay ningún comando que esperar hasta que finalice el proceso. 
# Pero podemos crear un bucle while que envíe la señal cont al proceso. 
#Esto tendrá éxito mientras el proceso exista, y falla una vez que el proceso desaparezca. 
#Dentro de este bucle while, simplemente agregaremos una llamada para dormir una, para esperar un segundo hasta la siguiente comprobación.

for pid in $(pidof chrome); do while kill -CONT $pid; do sleep 1; done; done

