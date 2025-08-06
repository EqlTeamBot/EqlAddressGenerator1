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
        f"👤 Имя: {fake.name()}\n"
        f"🏠 Адрес: {fake.address()}\n"
        f"📮 Почтовый индекс: {fake.postcode()}\n"
        f"📞 Телефон: {fake.phone_number()}"
    )

    await update.message.reply_text(fake_data)

# Запуск бота
if __name__ == '__main__':
    import os

    TOKEN = "8247864883:AAHEqKgOyPnvhnz0K4hRJsSgUKdj42STN-M"  # Замените на токен вашего бота
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("fake", fake_command))

    print("Бот запущен...")
    app.run_polling()