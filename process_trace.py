import csv
import os

def process_trace_file(input_file, output_file):
    with open(input_file, 'r') as f:
        with open(output_file, 'w', newline='') as out_f:
            writer = csv.writer(out_f)
            writer.writerow(['Timestamp', 'OperationType', 'SectorNumber', 'IOSize'])
            
            for line in f:
                if not line.strip():
                    continue
                    
                parts = line.strip().split()
                
                if len(parts) >= 8 and parts[5] == 'D':
                    timestamp = float(parts[3])
                    op_type = parts[6]
                    sector = parts[7]
                    io_size = parts[9]
                    writer.writerow([timestamp, op_type, sector, io_size])

def process_multiple_files():
    input_files = ['ssdtrace-00', 'ssdtrace-01', 'ssdtrace-02']
    for idx, input_file in enumerate(input_files):
        process_trace_file(input_file, f'preprocessed-{idx:02d}.csv')

if __name__ == '__main__':
    process_multiple_files() 