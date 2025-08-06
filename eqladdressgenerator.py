from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from faker import Faker

# Поддерживаемые локали
SUPPORTED_LOCALES = {
    'us': 'en_US',
    'uk': 'en_GB',
    'ru': 'ru_RU',
    'de': 'de_DE',
    'fr': 'fr_FR',
    'ae': 'en_US',       # ОАЭ (нет локали — используем английский)
    'at': 'de_AT',       # Австрия
    'au': 'en_AU',       # Австралия
    'ba': 'en_US',       # Босния (нет — используем en)
    'be': 'fr_BE',       # Бельгия (можно также nl_BE)
    'bg': 'bg_BG',       # Болгария
    'ca': 'en_CA',       # Канада
    'ch': 'de_CH',       # Швейцария
    'hk': 'en_US',       # Гонконг
    'cy': 'en_US',       # Кипр (нет локали — используем en)
    'cz': 'cs_CZ',       # Чехия
    'es': 'es_ES',       # Испания
    'fi': 'fi_FI',       # Финляндия
    'gr': 'el_GR',       # Греция
    'hr': 'hr_HR',       # Хорватия
    'hu': 'hu_HU',       # Венгрия
    'il': 'en_US',       # Израиль (нет — используем en)
    'it': 'it_IT',       # Италия
    'my': 'en_US',       # Малайзия
    'nl': 'nl_NL',       # Нидерланды
    'no': 'no_NO',       # Норвегия
    'nz': 'en_NZ',       # Новая Зеландия
    'pl': 'pl_PL',       # Польша
    'pt': 'pt_PT',       # Португалия
    'ro': 'ro_RO',       # Румыния
    'rs': 'en_US',       # Сербия (нет — используем en)
    'se': 'sv_SE',       # Швеция
    'sg': 'en_US',       # Сингапур
    'si': 'sl_SI',       # Словения
    'sk': 'sk_SK',       # Словакия
    'tr': 'tr_TR',       # Турция
}

# Команда /fake
async def fake_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    args = context.args

    if not args:
        await update.message.reply_text("⚠️ Использование: /fake [код страны]\nНапример: /fake us")
        return

    country_code = args[0].lower()

    if country_code not in SUPPORTED_LOCALES:
        await update.message.reply_text("❌ Страна не поддерживается. Доступные коды: " + ", ".join(SUPPORTED_LOCALES.keys()))
        return

    fake = Faker(SUPPORTED_LOCALES[country_code])

    fake_data = (
        f"👤 Имя:  {fake.name()}\n"
        f"🏠 Адрес:  {fake.address()}\n"
        f"📮 Почтовый индекс:  {fake.postcode()}\n"
        f"📞 Телефон:  {fake.phone_number()}"
    )

    await update.message.reply_text(fake_data)

# Запуск бота
if __name__ == '__main__':
    import os

    TOKEN = "8434706305:AAFGJ3NWORtUzgVTt0IlfCzFQDMWX_g7dUg"  # Замените на токен вашего бота
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("fake", fake_command))

    print("Бот запущен...")
    app.run_polling()