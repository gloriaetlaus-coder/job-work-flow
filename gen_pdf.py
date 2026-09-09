import asyncio
import os
from pyppeteer import launch

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

async def main():
    browser = await launch(headless=True, args=['--no-sandbox'])
    page = await browser.newPage()

    html_path = os.path.join(BASE_DIR, 'resume_general.html')
    await page.goto(f'file://{html_path}', {'waitUntil': 'networkidle0'})
    await page.waitForSelector('img')
    await asyncio.sleep(1)

    pdf_path = os.path.join(BASE_DIR, 'resume_general.pdf')
    await page.pdf({
        'path': pdf_path,
        'format': 'A4',
        'displayHeaderFooter': True,
        'headerTemplate': '<span></span>',
        'footerTemplate': '<div style="font-size:9px;color:#bbb;text-align:center;width:100%;padding-top:6px;"><span class="pageNumber"></span> / <span class="totalPages"></span></div>',
        'printBackground': True,
        'margin': {
            'top': '1.2cm',
            'bottom': '1.2cm',
            'left': '1.5cm',
            'right': '1.5cm',
        },
    })

    await browser.close()
    print(f'PDF generated: {pdf_path}')

asyncio.run(main())
