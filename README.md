## Projeto Pipeline de dados

### Grupo C

### Integrantes:
João Vitor Brogni - https://github.com/Jvbrogni <br>
João Vitor Rodrigues Rocha - https://github.com/JoaoVitorRodriguesRocha <br>
Lucas Fortunato Martins - https://github.com/lucasfm20 <br>

### Professor Orientador:

Jorge Luiz da Silva - https://github.com/jlsilva01


### Pré requisitos: 
- [Render](https://render.com/)
- [vsCode](https://code.visualstudio.com/)
- [Terraform](https://www.terraform.io/)
- [Azure CLI](https://learn.microsoft.com/pt-br/cli/azure/)

### Implantação
1- Crie uma conta paga na [Azure](https://portal.azure.com).

2- Clone o repositório.
```bash
git clone https://github.com/lucasfm20/ProjetoFinal_EngenhariaDeDados.git
```

3- Acesse a pasta iac no visual studio.

- 3.1 Efetue o login na Azure através do Azure CLI.
```bash
az login
```
- 3.2 Valide sua assinatura atual.
```bash
az account list -o table
```
- 3.3 Acessar a pasta iac/adls 

- 3.4 Rodar os comandos e inserir variáveis conforme solicitado.
```bash
terraform init
```

```bash
terraform validate
```

```bash
terraform fmt
```

```bash
terraform plan
```

```bash
terraform apply
```

- 3.5 Posteriormente rodar os mesmos comandos dentro da pasta iac/databricks

- 3.6 Logar no portal da [Azure](https://portal.azure.com) e conferir o deploy.

4- No portal da azure clique na sua conta de armazenamento e gere um SAS token com os tipos de recursos selecionados(Serviço,Contêiner,Objeto)

5- No databricks você deve copiar os notebooks de cada camada disponíveis na pasta convercaoBanco.

6- Inserir os scripts copiados em um notebook para cada camada.

7-Pode ser criado um job com tarefas individuais, ou apenas executado os notebooks.