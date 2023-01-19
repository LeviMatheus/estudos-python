from playwright.sync_api import sync_playwright

url_fluid = "https://0710.fluid.prd.sicredi.cloud/"

with sync_playwright() as pw:
    navegador = pw.chromium.launch()
    pagina = navegador.new_page()
    pagina.goto(url_fluid)
    print(f"URL atual: {pagina.title()}")
    navegador.close()