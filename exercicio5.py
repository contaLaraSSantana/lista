#Utilizando a lista de nomes em anexo, faça um programa que o usuário vai digitar um nome em seguida verifique se o nome
#digitado esta presente na lista se estiver envie um mensagem dizendo que o nome foi encontrado e finalize o programa.
#Caso não encontre peça para digitar novamente o nome.

nome = [
    'João', 'Maria', 'Pedro', 'Ana', 'Carlos', 'Mariana', 'José', 'Beatriz', 'Antônio', 'Laura',
    'Luiz', 'Camila', 'Fernando', 'Isabela', 'André', 'Manuela', 'Rafael', 'Gabriela', 'Marcos', 'Amanda',
    'Ricardo', 'Letícia', 'Marcelo', 'Clara', 'Paulo', 'Larissa', 'Rodrigo', 'Natália', 'Lucas', 'Carolina',
    'Guilherme', 'Juliana', 'Gustavo', 'Isabella', 'Maurício', 'Luana', 'Diego', 'Bianca', 'Leonardo', 'Carla',
    'Hugo', 'Lorena', 'Raul', 'Fernanda', 'Alexandre', 'Patrícia', 'Vitor', 'Priscila', 'Igor', 'Evelyn',
    'Arthur', 'Renata', 'Miguel', 'Gisele', 'Enzo', 'Thais', 'Ricardo', 'Vanessa', 'Júlio', 'Gabrielle',
    'Bruno', 'Mariane', 'César', 'Aline', 'Fábio', 'Bárbara', 'Marcos', 'Jéssica', 'Renato', 'Tatiana',
    'Samuel', 'Amanda', 'Eduardo', 'Vitória', 'Raphael', 'Nathalia', 'Caio', 'Daniela', 'Alex', 'Jaqueline',
    'Luís', 'Sabrina', 'Roberto', 'Paula', 'Douglas', 'Caroline', 'Adriano', 'Letícia', 'Vinícius', 'Julia',
    'Felipe', 'Fernanda', 'Bruno', 'Mirella', 'Rogério', 'Silvia', 'Thiago', 'Simone', 'Jorge', 'Monique',
    'Leandro', 'Michelle', 'William', 'Renata', 'Gustavo', 'Luciana', 'Matheus', 'Eliane', 'Victor', 'Cristina',
    'Marcelo', 'Lívia', 'Diego', 'Pamela', 'Nelson', 'Angélica', 'André', 'Rafaela', 'Rafael', 'Cíntia',
    'Rodrigo', 'Renata', 'Paulo', 'Giovanna', 'Ricardo', 'Luciana', 'Adriano', 'Sandra', 'Carlos', 'Márcia',
    'Lucas', 'Marina', 'Maurício', 'Cecília', 'Alexandre', 'Viviane', 'Renato', 'Heloisa', 'Bruno', 'Elisa',
    'Fábio', 'Denise', 'Igor', 'Isabela', 'Arthur', 'Mariana', 'Miguel', 'Carolina', 'Enzo', 'Luiza',
    'Caio', 'Bianca', 'Vítor', 'Talita', 'Rafael', 'Carla', 'Luís', 'Mônica', 'Eduardo', 'Larissa',
    'Leandro', 'Lorena', 'William', 'Manuela', 'Fernando', 'Gisele', 'Gustavo', 'Paula', 'Felipe', 'Monique',
    'Rodrigo', 'Daniela', 'Marcelo', 'Natália', 'Thiago', 'Isabella', 'Renato', 'Larissa', 'Ricardo', 'Mirella',
    'Júlio', 'Sabrina', 'Marcos', 'Patrícia', 'Adriano', 'Aline', 'Hugo', 'Fernanda', 'Bruno', 'Clara',
    'Douglas', 'Jéssica', 'Nelson', 'Gabriela', 'André', 'Priscila', 'Alex', 'Camila', 'Diego', 'Renata',
    'Felipe', 'Letícia', 'Rogério', 'Daniela', 'Matheus', 'Mariana', 'Raphael', 'Giovanna', 'Lucas', 'Luciana',
    'Leandro', 'Carolina', 'Fábio', 'Luiza', 'Samuel', 'Bianca', 'Nelson', 'Carla', 'Igor', 'Mônica',
    'Thiago', 'Lorena', 'Paulo', 'Manuela', 'Renato', 'Vanessa', 'Roberto', 'Camila', 'Adriano', 'Aline',
    'Douglas', 'Fernanda', 'Júlio', 'Clara', 'William', 'Patrícia', 'Gustavo', 'Jéssica', 'Matheus', 'Letícia',
    'André', 'Gabriela', 'Felipe', 'Priscila', 'Rogério', 'Daniela', 'Marcos', 'Natália', 'Renato', 'Isabella',
    'Hugo', 'Larissa', 'Fábio', 'Gisele', 'Arthur', 'Michelle', 'Raphael', 'Monique', 'Lucas', 'Paula',
    'Luís', 'Lívia', 'Victor', 'Cecília', 'Leandro', 'Mariana', 'Diego', 'Carolina', 'Felipe', 'Luiza',
    'Renato', 'Bianca', 'Miguel', 'Carla', 'Eduardo', 'Mônica', 'Rodrigo', 'Lorena', 'Caio', 'Manuela',
    'Thiago', 'Vanessa', 'Paulo', 'Camila', 'Ricardo', 'Aline', 'Adriano', 'Fernanda', 'Bruno', 'Clara',
    'Gustavo', 'Patrícia', 'Matheus', 'Jéssica', 'Rogério', 'Letícia', 'André', 'Gabriela', 'Felipe', 'Priscila',
    'Renato', 'Daniela', 'Arthur', 'Isabella', 'Hugo', 'Larissa', 'Fábio', 'Gisele', 'Raphael', 'Michelle',
    'Lucas', 'Monique', 'Victor', 'Paula', 'Leandro', 'Lívia', 'Diego', 'Cecília', 'Renato', 'Mariana',
    'Miguel', 'Carolina', 'Eduardo', 'Bianca', 'Rodrigo', 'Mônica', 'Caio', 'Lorena', 'Thiago', 'Manuela',
    'Paulo', 'Vanessa', 'Ricardo', 'Camila', 'Adriano', 'Aline', 'Gustavo', 'Fernanda', 'Bruno', 'Clara',
    'Matheus', 'Patrícia', 'Rogério', 'Jéssica', 'Felipe', 'Letícia', 'André', 'Priscila', 'Arthur', 'Daniela',
    'Hugo', 'Isabella', 'Raphael', 'Larissa', 'Lucas', 'Gisele', 'Leandro', 'Michelle', 'Victor', 'Monique',
    'Diego', 'Paula', 'Renato', 'Lívia', 'Miguel', 'Cecília', 'Eduardo', 'Carolina', 'Rodrigo', 'Bianca',
    'Caio', 'Mônica', 'Thiago', 'Lorena', 'Ricardo', 'Manuela', 'Paulo', 'Camila', 'Adriano', 'Aline',
    'Gustavo', 'Fernanda', 'Bruno', 'Clara', 'Matheus', 'Patrícia', 'Rogério', 'Jéssica', 'Felipe', 'Letícia',
    'André', 'Priscila', 'Arthur', 'Daniela', 'Hugo', 'Isabella', 'Raphael', 'Larissa', 'Lucas', 'Gisele',
    'Leandro', 'Michelle', 'Victor', 'Monique', 'Diego', 'Paula', 'Renato', 'Lívia', 'Miguel', 'Cecília',
    'Eduardo', 'Carolina', 'Rodrigo', 'Bianca', 'Caio', 'Mônica', 'Thiago', 'Lorena', 'Ricardo', 'Manuela',
    'Paulo', 'Camila', 'Adriano', 'Aline', 'Gustavo', 'Fernanda', 'Bruno', 'Clara', 'Matheus', 'Patrícia',
    'Rogério', 'Jéssica', 'Felipe', 'Letícia', 'André', 'Priscila', 'Arthur', 'Daniela', 'Hugo', 'Isabella',
    'Raphael', 'Larissa', 'Lucas', 'Gisele', 'Leandro', 'Michelle', 'Victor', 'Monique', 'Diego', 'Paula',
    'Renato', 'Lívia', 'Miguel', 'Cecília', 'Eduardo', 'Carolina', 'Rodrigo', 'Bianca', 'Caio', 'Mônica',
    'Thiago', 'Lorena', 'Ricardo', 'Manuela', 'Paulo', 'Camila', 'Adriano', 'Aline', 'Gustavo', 'Fernanda',
    'Bruno', 'Clara', 'Matheus', 'Patrícia', 'Rogério', 'Jéssica', 'Felipe', 'Letícia', 'André', 'Priscila',
    'Arthur', 'Daniela', 'Hugo', 'Isabella', 'Raphael', 'Larissa', 'Lucas', 'Gisele', 'Leandro', 'Michelle',
    'Victor', 'Monique', 'Diego', 'Paula', 'Renato', 'Lívia', 'Miguel', 'Cecília', 'Eduardo', 'Carolina',
    'Rodrigo', 'Bianca', 'Caio', 'Mônica', 'Thiago', 'Lorena', 'Ricardo', 'Manuela', 'Paulo', 'Camila',
    'Adriano', 'Aline', 'Gustavo', 'Fernanda', 'Bruno', 'Clara', 'Matheus', 'Patrícia', 'Rogério', 'Jéssica',
    'Felipe', 'Letícia', 'André', 'Priscila', 'Arthur', 'Daniela', 'Hugo', 'Isabella', 'Raphael', 'Larissa',
    'Lucas', 'Gisele', 'Leandro', 'Michelle', 'Victor', 'Monique', 'Diego', 'Paula', 'Renato', 'Lívia',
    'Miguel', 'Cecília', 'Eduardo', 'Carolina', 'Rodrigo', 'Bianca', 'Caio', 'Mônica', 'Thiago', 'Lorena',
    'Ricardo', 'Manuela', 'Paulo', 'Camila', 'Adriano', 'Aline', 'Gustavo', 'Fernanda', 'Bruno', 'Clara',
    'Matheus', 'Patrícia', 'Rogério', 'Jéssica', 'Felipe', 'Letícia', 'André', 'Priscila', 'Arthur', 'Daniela',
    'Hugo', 'Isabella', 'Raphael', 'Larissa', 'Lucas', 'Gisele', 'Leandro', 'Michelle', 'Victor', 'Monique',
    'Diego', 'Paula', 'Renato', 'Lívia', 'Miguel', 'Cecília', 'Eduardo', 'Carolina', 'Rodrigo', 'Bianca',
    'Caio', 'Mônica', 'Thiago', 'Lorena', 'Ricardo', 'Manuela', 'Paulo', 'Camila', 'Adriano', 'Aline',
    'Gustavo', 'Fernanda', 'Bruno', 'Clara', 'Matheus', 'Patrícia', 'Rogério', 'Jéssica', 'Felipe', 'Letícia',
    'André', 'Priscila', 'Arthur', 'Daniela', 'Hugo', 'Isabella', 'Raphael', 'Larissa', 'Lucas', 'Gisele',
    'Leandro', 'Michelle', 'Victor', 'Monique', 'Diego', 'Paula', 'Renato', 'Lívia', 'Miguel', 'Cecília',
    'Eduardo', 'Carolina', 'Rodrigo', 'Bianca', 'Caio', 'Mônica', 'Thiago', 'Lorena', 'Ricardo', 'Manuela',
    'Paulo', 'Camila', 'Adriano', 'Aline', 'Gustavo', 'Fernanda', 'Bruno', 'Clara', 'Matheus', 'Patrícia',
    'Rogério', 'Jéssica', 'Felipe', 'Letícia', 'André', 'Priscila', 'Arthur', 'Daniela', 'Hugo', 'Isabella',
    'Raphael', 'Larissa', 'Lucas', 'Gisele', 'Leandro', 'Michelle', 'Victor', 'Monique', 'Diego', 'Paula',
    'Renato', 'Lívia', 'Miguel', 'Cecília', 'Eduardo', 'Carolina', 'Rodrigo', 'Bianca', 'Caio', 'Mônica',
    'Thiago', 'Lorena', 'Ricardo', 'Manuela', 'Paulo', 'Camila', 'Adriano', 'Aline', 'Gustavo', 'Fernanda',
    'Bruno', 'Clara', 'Matheus', 'Patrícia', 'Rogério', 'Jéssica', 'Felipe', 'Letícia', 'André', 'Priscila',
    'Arthur', 'Daniela', 'Hugo', 'Isabella', 'Raphael', 'Larissa', 'Lucas', 'Gisele', 'Leandro', 'Michelle',
    'Victor', 'Monique', 'Diego', 'Paula', 'Renato', 'Lívia', 'Miguel', 'Cecília', 'Eduardo', 'Carolina',
    'Rodrigo', 'Bianca', 'Caio', 'Mônica', 'Thiago', 'Lorena', 'Ricardo', 'Manuela', 'Paulo', 'Camila',
    'Adriano', 'Aline', 'Gustavo', 'Fernanda', 'Bruno', 'Clara', 'Matheus', 'Patrícia', 'Rogério', 'Jéssica',
    'Felipe', 'Letícia', 'André', 'Priscila', 'Arthur', 'Daniela', 'Hugo', 'Isabella', 'Raphael', 'Larissa',
    'Lucas', 'Gisele', 'Leandro', 'Michelle', 'Victor', 'Monique', 'Diego', 'Paula', 'Renato', 'Lívia',
    'Miguel', 'Cecília', 'Eduardo', 'Carolina', 'Rodrigo', 'Bianca', 'Caio', 'Mônica', 'Thiago', 'Lorena',
    'Ricardo', 'Manuela', 'Paulo', 'Camila', 'Adriano', 'Aline', 'Gustavo', 'Fernanda', 'Bruno', 'Clara',
    'Matheus', 'Patrícia', 'Rogério', 'Jéssica', 'Felipe', 'Letícia', 'André', 'Priscila', 'Arthur', 'Daniela',
    'Hugo', 'Isabella', 'Raphael', 'Larissa', 'Lucas', 'Gisele', 'Leandro', 'Michelle', 'Victor', 'Monique',
    'Diego', 'Paula', 'Renato', 'Lívia', 'Miguel', 'Cecília', 'Eduardo', 'Carolina', 'Rodrigo', 'Bianca',
    'Caio', 'Mônica', 'Thiago', 'Lorena', 'Ricardo', 'Manuela', 'Paulo', 'Camila', 'Adriano', 'Aline',
    'Gustavo', 'Fernanda', 'Bruno', 'Clara', 'Matheus', 'Patrícia', 'Rogério', 'Jéssica', 'Felipe', 'Letícia',
    'André', 'Priscila', 'Arthur', 'Daniela', 'Hugo', 'Isabella', 'Raphael', 'Larissa', 'Lucas', 'Gisele',
    'Leandro', 'Michelle', 'Victor', 'Monique', 'Diego', 'Paula', 'Renato', 'Lívia', 'Miguel', 'Cecília',
    'Eduardo', 'Carolina', 'Rodrigo', 'Bianca', 'Caio', 'Mônica', 'Thiago', 'Lorena', 'Ricardo', 'Manuela',
    'Paulo', 'Camila', 'Adriano', 'Aline', 'Gustavo', 'Fernanda', 'Bruno', 'Clara', 'Matheus', 'Patrícia',
    'Rogério', 'Jéssica', 'Felipe', 'Letícia', 'André', 'Priscila', 'Arthur', 'Daniela', 'Hugo', 'Isabella',
    'Raphael', 'Larissa', 'Lucas', 'Gisele', 'Leandro', 'Michelle', 'Victor', 'Monique', 'Diego', 'Paula',
    'Renato', 'Lívia', 'Miguel', 'Cecília', 'Eduardo', 'Carolina', 'Rodrigo', 'Bianca', 'Caio', 'Mônica',
    'Thiago', 'Lorena', 'Ricardo', 'Manuela', 'Paulo', 'Camila', 'Adriano', 'Aline', 'Gustavo', 'Fernanda']

p=input("Digite um nome:")
if p in nome:
    print(f' O nome {p} está presente na lista')
else:
    print(f' Nome não encontrado')