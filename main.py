import requests

def get_public_ip():
    try:
        response = requests.get('https://api.ipify.org?format=json')
        if response.status_code == 200:
            return response.json()['ip']
        return None
    except Exception as e:
        print(f"Gagal mendapatkan IP: {e}")
        return None

def get_ip_location(ip_address):
    try:
        response = requests.get(f'http://ip-api.com/json/{ip_address}')
        if response.status_code == 200:
            data = response.json()
            return data
        return None
    except Exception as e:
        print(f"Gagal mendapatkan lokasi: {e}")
        return None

if __name__ == "__main__":
    ip = get_public_ip()
    
    if ip:
        print(f"IP Address Anda: {ip}")
        
        location_info = get_ip_location(ip)
        
        if location_info and location_info['status'] == 'success':
            print("\nInformasi Lokasi:")
            print(f"Negara: {location_info['country']}")
            print(f"Kode Negara: {location_info['countryCode']}")
            print(f"Wilayah: {location_info['regionName']}")
            print(f"Kota: {location_info['city']}")
            print(f"Kode Pos: {location_info['zip']}")
            print(f"Koordinat: Lat {location_info['lat']}, Lon {location_info['lon']}")
            print(f"Zona Waktu: {location_info['timezone']}")
            print(f"ISP: {location_info['isp']}")
        else:
            print("Tidak dapat mendapatkan informasi lokasi")
    else:
        print("Tidak dapat mendapatkan IP Address")