#Попова Елена, 10 когорта, Финальный проект, Инженер по тестированию плюс

# Логическое описание решений:
# 1.Создание ключей:
$ ssh-keygen
Generating public/private rsa key pair.
Enter file in which to save the key (/home/Елена/.ssh/id_rsa):
/home/Елена/.ssh/id_rsa already exists.
Overwrite (y/n)? y
Enter passphrase (empty for no passphrase):
Enter same passphrase again:

#2.Вывод публичного ключа:
$ cat ~/.ssh/id_rsa.pub
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQC9+VAT6d6I5gxGDeST70DTfIxThCswjDj5k7PJClvhRKg+ooWLaHNoVipK6vhWtq3fd61siwFa5zofMSnzwQaDJUCEUL3LOs1M9kbjSX7x4eo31HnsU76GwmcsiVX5yiH+uuDFfI1p3sNlKBeHXi9wFd04HGzj3/6ASuAqaFjh7Atn/nDij6agYaNAIpUz+iCYY/Rlo7OxfLrXc6jKWFkibP6+XRRkVulsffvg9XiCV77R2377LLNQxyjwGhlFYlHJfgRotI8SCmdAzfaBcrZGmJc0JpwdyxvTYUBMRcyyka+R5TEp+OoKwvNkYbLFhnUI3Rdupd+zTonWujYMEbjqmLXXv23H33s4MjI2N7jiOvhKQGCqWN8uHx85o0QkbRbvdeL0l4SriXHIW9umnTQPshPda6eRLUBJkrXvWo1AzQ4WnMgcLYa1WlCzVjLC1vSI0J1S5v3UzRc8YjaaH9GaY2Qc+nEAPu3VlkHXZHCtd13C7dHI3sE8gzz5aIKY0fE= Елена@LAPTOP-KS9MRGL0


#3. Подключение к удалённому серверу:
$ ssh daea1ad7-9d27-4f9c-9fa8-f7d99bd5359a@serverhub.praktikum-services.ru -p 4554


#4. Подключение к базе данных:
$ psql -U morty -d scooter_rent

#Пароль: smith.

#Задание 1:

SELECT c.login,count (o."inDelivery")
FROM “Couriers” AS c
INNER JOIN “Orders” AS o ON c.id=o.”courierId”;
WHERE o."inDelivery" = true

#Задание 2:

SELECT track,
    CASE
        WHEN 'finished' == true THEN '2'
        WHEN 'canсelled' == true THEN '-1'
        WHEN 'inDelivery' == true THEN '1'
        ELSE '0'
    END
FROM “Orders”