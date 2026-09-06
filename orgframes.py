import os
import shutil
import argparse
import glob

def org_frames(folder_name, ninout, inout, delete_originals):
	current_dir = os.getcwd()
	
	# Identifica os frames (.png) e ordena-os
	search_pattern = os.path.join(current_dir, "*.png")
	frames = sorted(glob.glob(search_pattern))
	
	if not frames:
		print("Erro: Nenhum arquivo .png encontrado nesta pasta.")
		return

	total_frames = len(frames)
	print(f"{total_frames} frames encontrados.")

	# Lógica para criar pastas e distribuir arquivos
	if ninout:
		main_folder = os.path.join(current_dir, folder_name)
		inout = True  # Força a criação das pastas -in e -out
		
	if inout:
		dir = current_dir if not ninout else main_folder
		in_folder = os.path.join(dir, f"{folder_name}-in")
		out_folder = os.path.join(dir, f"{folder_name}-out")
		
		os.makedirs(in_folder, exist_ok=True)
		os.makedirs(out_folder, exist_ok=True)
		
		print(f"Criando pastas: '{folder_name}-in' e '{folder_name}-out'")
		
		for i, frame_path in enumerate(frames):
			original_filename = os.path.basename(frame_path)
			
			# -in (ordem normal)
			shutil.copy(frame_path, os.path.join(in_folder, original_filename))
			
			# -out (ordem inversa)
			inverse_index = total_frames - i
			inverse_filename = f"{inverse_index:04d}.png"
			shutil.copy(frame_path, os.path.join(out_folder, inverse_filename))
			
		print("Frames organizados e invertidos com sucesso!")

	else:
		# Cria apenas 1 pasta
		destination_folder = os.path.join(current_dir, folder_name)
		os.makedirs(destination_folder, exist_ok=True)
		
		print(f"Criando pasta: '{folder_name}'")
		
		for frame_path in frames:
			original_filename = os.path.basename(frame_path)
			shutil.copy(frame_path, os.path.join(destination_folder, original_filename))
			
		print("Frames copiados com sucesso!")

	if delete_originals:
		for frame_path in frames:
			os.remove(frame_path)
		print("Frames originais apagados.")

	print("Organização de frames concluída.")

if __name__ == "__main__":
	parser = argparse.ArgumentParser(description="Organizador de frames do Blender.")
	parser.add_argument("nome",    help="O nome base da pasta a ser criada.")
	parser.add_argument("-ninout", action="store_true", help="Cria a pasta principal e as subpastas -in e -out (com ordem inversa).")
	parser.add_argument("-inout",  action="store_true", help="Cria as pastas -in e -out e inverte a ordem na -out.")
	parser.add_argument("-d",      action="store_true", help="Apaga os frames originais da raiz após a cópia.")
	
	args = parser.parse_args()
	
	org_frames(args.nome, args.ninout, args.inout, args.d)