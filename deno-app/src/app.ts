import { Server, IContext } from 'https://github.com/fen-land/deno-fen/raw/master/server.ts'
import { Router } from 'https://github.com/fen-land/deno-fen/raw/master/tool/router.ts'
import { process } from 'https://deno.land/std/node/process.ts'

const daprPort = process.env.DAPR_HTTP_PORT || 3500
const stateStoreName = `statestore`
const stateUrl = `http://localhost:${daprPort}/v1.0/state/${stateStoreName}`
const port = 3001

const app = new Server()

const router = new Router()

router
    .get('/order', async (context: IContext) => {
        try {
            const response = await fetch(`${stateUrl}/order`)
            if (!response.ok) {
                throw 'Could not get state.'
            }

            context.body = await response.text()
            context.status = 200
            console.log(context.body)
        } catch (error) {
            console.log(error)
            context.status = 500
            context.body = {message: error}
        }
    })
    .post('/neworder', async (context: IContext) => {
        const orderId = context.reqBody.data.orderId
        console.log(`Got a new order! Order ID: ${orderId}`)

        const state =[{
            key: 'order',
            value: context.reqBody.data
        }]

        try {
            const respose = await fetch(stateUrl, {
                method: 'POST',
                body: JSON.stringify(state),
                headers: {
                    'Content-Type': "application/json"
                }
            })

            if (!respose.ok) {
                throw 'Failed to persist state.'
            }

            console.log('Successfully persisted state.')
            context.body = '{}'
            context.status = 200
        } catch (error) {
            console.log(error)
            context.status = 500
            context.body = {message: error}
        }
    })
    

app.setController(router.controller)
app.port = port
app.logger.changeLevel('ALL')
app.start()
