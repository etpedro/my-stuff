https://services.github.com/on-demand/downloads/github-git-cheat-sheet.pdf

### Configuração global do Git
sudo apt-get install git
git config --global user.name "username
git config --global user.email "email address"

git add [ficheiro]					//Adiciona um ficheiro à área de preparação para que possa ser incluído em commits (staged)
git add .						//Adiciona todos os ficheiros à área de preparação para que possa ser incluído em commits (staged)
git status  						//Lista todos os ficheiros modificados no projecto atual
git diff						//Mostra as diferenças linha a linha dos ficheiros alterados (pre-stage)
git commit -m "Commit from Linux"			//Guarda as alterações preparadas permanentemente no histórico de versões
git push -u origin master				//Envia todos os commits do branch local para o GitHub
git pull						//Download e merge num só comando. Igual a executar: git fetch + git merge
							
git clone [url]							//Faz download de um projeto, incluindo toda a sua história
git init [nome-do-projeto]					//Cria um novo repositório local com o nome de projecto especificado
git remote add origin https://github.com/etpedro/my-stuff.git	//Adicionar origem remota a partir do URL. Nota: O repositorio foi criado no site
git remote -v							//Lista os repositórios remotos
git fetch origin master 					//Faz download de todo o histórico do repositório remoto, branch master


## Workflow tipico para criação de ficheiros locais e upload para o repositório. 

echo "Teste worflow" > teste.md				//criar ficheiro
git add teste.md					//Adiciona o ficheiro para a área de staging
git commit -m "Adicionado o file "testes.md""		//Aceita as alterações dos ficheiros que estão na área de staging para poderem ser enviados para o master
git push origin master					//Envia os ficheiros para o master

## Durante todos os passos podemos ir fazendo os seguintes comandos para ir validando o estado das áreas e os proximos passos
git diff

git status
