"""
SCRIPT PERSONALIZADO COMPLETO DE LIMPIEZA PARA ventas_techventas.csv
====================================================================
Soluciona: encoding, comillas, valores nulos, negativos y duplicados

Ing. Jorge Uriel liévano Cifuentes
viernes 19 de junio de 2026
Bucaramanga - Colombia - UDES
"""

import pandas as pd
import re
import csv
from pathlib import Path

def limpiar_csv_completo(ruta_entrada, ruta_salida=None):
    """
    Limpieza completa del CSV:
    1. Corrige encoding (Ana Lï¿½ï¿ → Ana López)
    2. Repara comillas mal formadas
    3. Maneja valores nulos
    4. Corrige cantidades negativas
    5. Elimina duplicados
    """
    
    print("="*70)
    print("🚀 LIMPIEZA COMPLETA DE CSV")
    print("="*70)
    
    # 1. LEER EL ARCHIVO COMO TEXTO Y REPARAR ENCODING
    # =================================================
    print("\n📂 Paso 1: Leyendo y reparando encoding...")
    
    with open(ruta_entrada, 'r', encoding='latin1') as f:
        contenido = f.read()
    
    # 2. REPARAR ENCODING (Ana Lï¿½ï¿ → Ana López)
    # ===========================================
    print("🔧 Paso 2: Reparando encoding...")
    
    # Patrón para detectar caracteres corruptos
    # Buscar "Ana L" seguido de caracteres extraños
    patron_encoding = r'Ana L[^\w\s,]+'
    contenido = re.sub(patron_encoding, 'Ana López', contenido)
    
    # También reparar otras variantes
    contenido = contenido.replace('Ana L챦쩔쩍챦쩔', 'Ana López')
    contenido = contenido.replace('Ana Lï¿½ï¿', 'Ana López')
    
    # 3. REPARAR COMILLAS MAL FORMADAS
    # =================================
    print("🔧 Paso 3: Reparando comillas mal formadas...")
    
    # Estrategia: Eliminar las comillas que envuelven toda la línea
    # y reemplazar comillas dobles internas por comillas simples
    lineas = contenido.split('\n')
    lineas_reparadas = []
    
    for linea in lineas:
        if not linea.strip():
            continue
            
        # Si la línea empieza y termina con comillas
        if linea.startswith('"') and linea.endswith('"'):
            # Quitar las comillas externas
            linea = linea[1:-1]
            # Reemplazar "" internas por "
            linea = linea.replace('""', '"')
        
        # Si la línea tiene comillas internas mal formadas
        if '"' in linea:
            # Reemplazar comillas que no están al inicio o final
            # pero que están dentro de campos de texto
            partes = linea.split(',')
            partes_reparadas = []
            
            for parte in partes:
                # Si la parte tiene comillas pero no es un campo completo
                if '"' in parte and not (parte.startswith('"') and parte.endswith('"')):
                    parte = parte.replace('"', '')
                partes_reparadas.append(parte)
            
            linea = ','.join(partes_reparadas)
        
        lineas_reparadas.append(linea)
    
    contenido = '\n'.join(lineas_reparadas)
    
    # 4. GUARDAR ARCHIVO TEMPORAL
    # ============================
    print("💾 Paso 4: Guardando archivo temporal...")
    
    ruta_temp = ruta_entrada.replace('.csv', '_temp.csv')
    with open(ruta_temp, 'w', encoding='utf-8') as f:
        f.write(contenido)
    
    # 5. CARGAR CON PANDAS
    # ====================
    print("📊 Paso 5: Cargando con pandas...")
    
    df = pd.read_csv(
        ruta_temp,
        encoding='utf-8',
        quotechar='"',
        doublequote=True,
        parse_dates=['fecha']
    )
    
    # 6. LIMPIAR DATOS CON PANDAS
    # ============================
    print("🧹 Paso 6: Limpiando datos con pandas...")
    
    # 6.1 Eliminar espacios en blanco
    columnas_texto = df.select_dtypes(include=['object']).columns
    for col in columnas_texto:
        df[col] = df[col].str.strip()
    
    # 6.2 Manejar valores nulos
    print("   - Valores nulos antes:")
    print(df.isnull().sum())
    
    # Rellenar nulos en 'producto'
    df['producto'] = df['producto'].fillna('Desconocido')
    
    # 6.3 Corregir cantidades negativas
    df['cantidad'] = df['cantidad'].abs()
    
    # 6.4 Eliminar duplicados
    df = df.drop_duplicates(subset=['order_id'])
    
    # 6.5 Convertir tipos
    df['order_id'] = df['order_id'].astype(int)
    df['cantidad'] = df['cantidad'].astype(int)
    df['precio_unitario'] = df['precio_unitario'].astype(float)
    df['descuento'] = df['descuento'].astype(float)
    
    # 6.6 Crear columna de ingreso
    df['ingreso'] = df['cantidad'] * df['precio_unitario'] * (1 - df['descuento'])
    
    # 7. GUARDAR ARCHIVO FINAL
    # ========================
    print("💾 Paso 7: Guardando archivo final...")
    
    if ruta_salida is None:
        ruta_salida = ruta_entrada.replace('.csv', '_clean.csv')
    
    df.to_csv(ruta_salida, index=False, encoding='utf-8')
    
    # 8. ELIMINAR ARCHIVO TEMPORAL
    # ============================
    import os
    if os.path.exists(ruta_temp):
        os.remove(ruta_temp)
    
    # 9. MOSTRAR RESULTADOS
    # =====================
    print("\n" + "="*70)
    print("📊 RESULTADOS DE LA LIMPIEZA")
    print("="*70)
    
    print(f"✅ Registros originales: {len(df)}")
    print(f"📋 Columnas: {df.columns.tolist()}")
    
    # Verificar encoding
    print("\n🔍 Verificando nombres de vendedores:")
    print(f"   Vendedores únicos: {df['vendedor'].unique().tolist()}")
    
    # Verificar producto con comillas
    print("\n🔍 Verificando productos con comillas:")
    productos_con_comillas = df[df['producto'].str.contains('"', na=False)]
    if len(productos_con_comillas) > 0:
        print(f"   ✅ Productos con comillas: {len(productos_con_comillas)}")
        for idx, row in productos_con_comillas.iterrows():
            print(f"   - {row['order_id']}: {row['producto']}")
    
    # Verificar orden problemática
    print("\n🔍 Verificando orden 1003 (problema original):")
    orden_1003 = df[df['order_id'] == 1003]
    if len(orden_1003) > 0:
        print(f"   ✅ Orden 1003 encontrada:")
        print(f"   - Producto: {orden_1003.iloc[0]['producto']}")
        print(f"   - Vendedor: {orden_1003.iloc[0]['vendedor']}")
        print(f"   - Cantidad: {orden_1003.iloc[0]['cantidad']}")
    
    print(f"\n✅ Archivo limpio guardado en: {ruta_salida}")
    
    return df


# ============================================
# EJECUCIÓN PRINCIPAL
# ============================================

if __name__ == "__main__":
    
    # Ruta del archivo original
    ruta_original = '../data/ventas_techventas.csv'
    
    # Ejecutar limpieza
    df_limpio = limpiar_csv_completo(ruta_original)
    
    # Mostrar muestra final
    print("\n👤 Muestra de datos limpios (primeras 5 filas):")
    print(df_limpio.head())
    
    # Estadísticas finales
    print("\n📈 Estadísticas de calidad:")
    print(f"   - Valores nulos: {df_limpio.isnull().sum().sum()}")
    print(f"   - Productos únicos: {df_limpio['producto'].nunique()}")
    print(f"   - Clientes únicos: {df_limpio['cliente_id'].nunique()}")