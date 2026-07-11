// src/infrastructure/factories/product.factory.ts
import { AxiosProductRepository } from '@/infrastructure/adapters/xios-product.repository'
import { ProductUseCase } from '@/application/use-cases/product.use-case'

export const productUseCase = new ProductUseCase(new AxiosProductRepository())