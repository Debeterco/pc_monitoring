import sqlite3
import time 
import random
from datetime import datetime

def init_db():
    conn = sqlite3.connect('pcs.db', timeout=10)
    cursor = conn.cursor()
    cursor.execute("PRAGMA journal_mode=WAL;")
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS leituras_pcs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp DATETIME,
            pc_id TEXT,
            uso_cpu REAL,
            uso_ram REAL,
            temp_cpu REAL
        )
    ''')
    conn.commit()
    conn.close()
    
def simular_pcs():
    init_db()
    print("Simulador de pcs em execução. Pressione Ctrl + C para parar")
    # Poderia adicionar mais PCs
    pcs = {
        'Pc_1': {'uso_cpu': 24.0, 'uso_ram': 55.0, 'temp_cpu': 60.2},
        'Pc_2': {'uso_cpu': 28.5, 'uso_ram': 48.0, 'temp_cpu': 50.8},
        'Pc_3': {'uso_cpu': 54.0, 'uso_ram': 62.0, 'temp_cpu': 53.1}
    }
    while True:
        try:
            conn = sqlite3.connect('pcs.db', timeout=10)
            cursor = conn.cursor()
        
            for pc_id, dados in pcs.items():
                uso_cpu = round(dados['uso_cpu'] + random.uniform(-0.4, 0.4), 2)
                uso_ram = round(max(0, min(100, dados['uso_ram'] + random.uniform(-0.8, 0.8))), 2)
                temp_cpu = round(dados['temp_cpu'] + random.uniform(-0.15, 0.15), 2)
                dados['uso_cpu'] = uso_cpu
                dados['uso_ram'] = uso_ram
                dados['temp_cpu'] = temp_cpu
                timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                
                cursor.execute('''
                    INSERT INTO leituras_pcs (timestamp, pc_id, uso_cpu, uso_ram, temp_cpu)
                    VALUES (?,?,?,?,?)
                ''', (timestamp, pc_id, uso_cpu, uso_ram, temp_cpu))
        
            conn.commit()
            conn.close()
            print(f"[{datetime.now().strftime('%H:%M:%S')}] Novas leituras inseridas.")
            time.sleep(2)
            
        except sqlite3.OperationalError as e:
            if "locked" in str(e).lower() or "busy" in str(e).lower():
                print(f"Aviso de concorrência: {e}")
                time.sleep(1)
            else:
                raise e
        except KeyboardInterrupt:
            print("\nSimulação finalizada")
            break
    
if __name__ == "__main__":
    simular_pcs()